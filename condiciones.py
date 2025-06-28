from abc import ABC, abstractmethod
from typing import Dict, List

import logging
from base import BaseConocimiento, OPERADORES, TipoComparacion, ElementoProposicion

logger = logging.getLogger("LOG")


class Condicion(ABC):
    def __init__(self, variables: List[str]):
        self.variables = variables

    @abstractmethod
    def validar(self, contexto: Dict[str, str], base: BaseConocimiento) -> bool:
        pass


class CondicionSimple(Condicion):
    def __init__(self, nombre_proposicion: str, variables: List[str]):
        super().__init__(variables)
        self.nombre_proposicion = nombre_proposicion

    def validar(self, contexto: Dict[str, str], base: BaseConocimiento) -> bool:
        if self.nombre_proposicion not in base.proposiciones:
            raise ValueError(f"Proposición '{self.nombre_proposicion}' no existe")
        parametros = []
        #Si es una variable, se sustituye por su valor en el contexto
        #Si no, se deja como está, puede ser un valor literal o individuo
        for i_contexto in contexto:
            for variable in self.variables:
                #si i_contexto es igual a la variable, se añade el valor de i_contexto al parametro. Si variable empieza por i_contexto seguido de punto, se busca el atributo en la variable
                if i_contexto == variable:
                    parametros.append(contexto[i_contexto])
                    break
                elif variable.startswith(i_contexto + "."):
                    #Si la variable es del tipo P.algo, se busca el atributo en el contexto
                    atributo = variable.split(".")[1]
                    if i_contexto in contexto:
                        parametros.append(contexto[i_contexto].atributos[atributo])
                    else:
                        raise ValueError(f"Variable '{i_contexto}' no encontrada en el contexto")
                    
                else:
                    parametros.append(variable)



        tupla = tuple(parametros)
        resultado = base.proposiciones[self.nombre_proposicion].existe(tupla)
        logger.debug(f"[{self.nombre_proposicion}] Validación simple {tupla} -> {resultado}")
        return resultado


class CondicionComparacion(Condicion):#REHACER
    def __init__(self, lado_izq, comparador: TipoComparacion, lado_der, variables: List[str]):
        super().__init__(variables)
        self.lado_izq = lado_izq
        self.lado_der = lado_der
        self.comparador = comparador

    def _resolver_valor(self, expr, contexto, base: BaseConocimiento):
        
        if isinstance(expr,(int,bool)):
            return expr

        nombre_variable,nombre_atributo = expr.split('.',1)
        if '.' in nombre_atributo:
            raise ValueError("[Punto no esperado]Un atributo no puede tener mas atributos")
        #nombre_variable,nombre_atributo = expr
        if not nombre_atributo:
            raise ValueError("[No atritbuot]Solo se puede comparar atributos")

        variable = contexto.get(nombre_variable)
        if variable is not None and isinstance(variable,ElementoProposicion):
            return variable.atributos[nombre_atributo]
        return variable 
 

    def validar(self, contexto: Dict[str, str], base: BaseConocimiento) -> bool:
        val_izq = self._resolver_valor(self.lado_izq, contexto, base)
        val_der = self._resolver_valor(self.lado_der, contexto, base)
        resultado = OPERADORES[self.comparador](val_izq, val_der)
        logger.debug(f"[Comparacion] {val_izq} {self.comparador.value} {val_der} -> {resultado}")
        return resultado


class CondicionLogica(Condicion):
    def __init__(self, condiciones: List[Condicion], operador: str):
        super().__init__([])
        self.condiciones = condiciones
        self.operador = operador
        for condicion in condiciones:
            for var_condicion in condicion.variables:
                if var_condicion not in self.variables:
                    self.variables.append(var_condicion)

    def validar(self, contexto: Dict[str, str], base: BaseConocimiento) -> bool:
        if self.operador == "AND":
            logger.debug(f"[CondicionLogica] Validando condiciones con AND")
            resultado = all(condicion.validar(contexto, base) for condicion in self.condiciones)
        elif self.operador == "OR":
            logger.debug(f"[CondicionLogica] Validando condiciones con OR")
            resultado = any(condicion.validar(contexto, base) for condicion in self.condiciones)
        else:
            raise ValueError(f"Operador lógico '{self.operador}' no reconocido")
        logger.debug(f"[CondicionLogica] Resultado {self.operador} -> {resultado}")
        return resultado
    
class CondicionNegacion(Condicion):
    def __init__(self, condicion: Condicion):
        super().__init__(condicion.variables)
        self.condicion = condicion

    def validar(self, contexto: Dict[str, str], base: BaseConocimiento) -> bool:
        logger.debug(f"[CondicionNegacion] Validando condición de negación")
        resultado = not self.condicion.validar(contexto, base)
        logger.debug(f"[CondicionNegacion] Resultado NOT -> {resultado}")
        return resultado
    
class CondicionAsignacion(Condicion):
    def __init__(self, variables: List, valiable_asignacion:str, nombre_proposicion: str):
        super().__init__(variables)
        self.variable_asignacion = valiable_asignacion#Nombre de la variable donde se guardará la asignación
        self.asignacion = []# Lista donde se guardarán las tuplas que coincidan con la proposición
        self.nombre_proposicion = nombre_proposicion
    def validar(self, contexto: Dict[str, str], base: BaseConocimiento) -> bool:
        if self.nombre_proposicion not in base.proposiciones:
            raise ValueError(f"Proposición '{self.nombre_proposicion}' no existe")
        

        parametros = []

        #CUIDADO!!! Puede haber casos en los que no se tenga que reiniciar la asignacion. Por ejemplo si hay una variable multiple en la condicion.
        #self.asignacion = [] #hay que reiniciar la asignación cada vez que se valida la condición
        #Si es una variable, se sustituye por su valor en el contexto
        #Si no, se deja como está, puede ser un valor literal o individuo
        for v in self.variables:
            if v not in contexto:
                parametros.append(v)
            else: 
                parametros.append(contexto[v])
        #Se debe de recorrer cada elemento de la proposicion, si los valores coinciden, se asigna el valor de la variable de asignación

        proposicion = base.proposiciones[self.nombre_proposicion]
        if not proposicion.elementos:
            logger.debug(f"[{self.nombre_proposicion}] No hay elementos en la proposición")
            return False
        if len(parametros) != proposicion.n:
            raise ValueError(f"Cantidad de parámetros {len(parametros)} no coincide con la cantidad de individuos de la proposición {proposicion.n}")
        for elemento in proposicion.elementos.values():
            #Se debe comprobar los parametros con el tupla del prop son iguales, si el parametro es "_" o "" se considera que coincide y  se añade esa tupla a la variable de asignación

            coincide = True
            for i, param in enumerate(parametros):
                if param not in ("_", "") and elemento.tupla[i] != param:
                    coincide = False
                    break
            if coincide:
                #Si coincide, se añade la tupla a la asignación
                
                self.asignacion.append(elemento)
        #Si no hay asignación, se devuelve False
        if not self.asignacion:
            logger.debug(f"[{self.nombre_proposicion}] No se encontraron coincidencias para la asignación")
            return False
        logger.debug(f"[{self.nombre_proposicion}] Validación de asignación {parametros} -> {self.asignacion}")
        return True

            
        