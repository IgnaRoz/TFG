from abc import ABC, abstractmethod
from typing import Dict, List

import logging
from base import BaseConocimiento, OPERADORES, TipoComparacion, ElementoProposicion, Variable
from func import func
#from motorEjecucion import motor

logger = logging.getLogger("LOG")


class Condicion(ABC):
    def __init__(self, variables: List[str]):
        self.variables = variables

    @abstractmethod
    def validar(self, contexto: Dict[str, str], base: BaseConocimiento) -> bool:
        pass


class CondicionSimple(Condicion):
    def __init__(self, nombre_proposicion: str, variables):
        super().__init__(variables)
        self.nombre_proposicion = nombre_proposicion

    def validar(self, contexto: Dict[str, str], base: BaseConocimiento) -> bool:
        if self.nombre_proposicion not in base.proposiciones:
            raise ValueError(f"Proposición '{self.nombre_proposicion}' no existe")
        parametros = []
        #Si es una variable, se sustituye por su valor en el contexto
        #Si no, se deja como está, puede ser un valor literal o individuo
        #for i_contexto in contexto:
        #    for variable in self.variables:
        #        #si i_contexto es igual a la variable, se añade el valor de i_contexto al parametro. Si variable empieza por i_contexto seguido de punto, se busca el atributo en la variable
        #        if i_contexto == variable:
        #            parametros.append(contexto[i_contexto])
        #            break
        #        elif variable.startswith(i_contexto + "."):
        #            #Si la variable es del tipo P.algo, se busca el atributo en el contexto
        #            atributo = variable.split(".")[1]
        #            if i_contexto in contexto:
        #                parametros.append(contexto[i_contexto].atributos[atributo])
        #            else:
        #                raise ValueError(f"Variable '{i_contexto}' no encontrada en el contexto")
        #            
        #        else:
        #            parametros.append(variable)

        #for variable in self.variables:
        #    aux = False
        #    for i_contexto in contexto:
        #        if i_contexto == variable:
        #            parametros.append(contexto[i_contexto])
        #            aux = True
        #            break
        #        elif variable.startswith(i_contexto+'.'):
        #            var, atributo = variable.split('.',1)
        #            if var == i_contexto and atributo in contexto[i_contexto].atributos:
        #                parametros.append(contexto[i_contexto].atributos[atributo])
        #                aux = True
        #                break
        #    if not aux:                    
        #        parametros.append(variable)
#


        for variable in self.variables:


            if isinstance(variable,Variable):
                if variable.nombre not in contexto:
                    raise ValueError(f"La varaible {variable.nobmre} no esta en el contexto")
                if variable.atributo is not None:
                    if variable.atributo not in contexto[variable.nombre].atributos:
                        raise ValueError(f"La variable {variable.nobmre} no tiene el atributo {variable.atributo}")
                    parametros.append(contexto[variable.nombre].atributos[variable.atributo])
                else:
                    parametros.append(contexto[variable.nombre])
            elif isinstance(variable,func) :
                #Se podria refactorizar
                parametros_funcion = []
                args = variable.args or []
                for arg in args:
                    if isinstance(arg,Variable):
                        if arg.nombre not in contexto: 
                           raise ValueError(f"No se ha econtrado la variable {arg} en el contexto")
                        if arg.atributo is not None : 
                            if arg.atributo not  in contexto[arg.nombre].atributo:
                                raise ValueError(f"No se ha econtrado el atributo {arg.atributo} en la variable {arg}")
                            parametros_funcion.append(contexto[arg.nombre].atributos[arg.atributo])
                        else:
                            parametros_funcion.append(contexto[arg.nombre])
                    else:
                        parametros_funcion.append(arg)
                parametros.append(variable.run(*args))
            else:
                #Se considera que es un tipo basico
                parametros.append(variable)
                




        tupla = tuple(parametros)
        resultado = base.proposiciones[self.nombre_proposicion].existe(tupla)
        logger.debug(f"[Condicion Simple] Validación simple de la proposicion {self.nombre_proposicion} con valores {tupla} y resultado {resultado}")
        return resultado

class CondicionFuncion(Condicion):
    def __init__(self, variables,funcion):
        super().__init__(variables)
        self.funcion = funcion

    def validar(self,contexto,base):



        parametros = []
        for var in self.variables:
            if isinstance(var,Variable):
                if var.nombre not in contexto:
                    raise ValueError(f"No se ha econtrado la variable {var} en el contexto")
                if var.atributo is not None : 
                    if var.atributo not  in contexto[var.nombre].atributos:
                        raise ValueError(f"No se ha econtrado el atributo {var.atributo} en la variable {var}")
                    parametros.append(contexto[var.nombre].atributos[var.atributo])
                else:
                    parametros.append(contexto[var.nombre])
            else:
                parametros.append(var)
        parametros = tuple(parametros)

        return self.funcion.run(*parametros)


class CondicionComparacion(Condicion):
    def __init__(self, lado_izq, comparador: TipoComparacion, lado_der, variables: List[str]):
        super().__init__(variables)
        self.lado_izq = lado_izq
        self.lado_der = lado_der
        self.comparador = comparador

    def _resolver_valor(self, expr, contexto, base: BaseConocimiento):
        

        if isinstance(expr,Variable):
            if expr.nombre not in contexto:
                    raise ValueError(f"La varaible {expr.nombre} no esta en el contexto")
            if expr.atributo is not None:
                if expr.atributo not in contexto[expr.nombre].atributos:
                    raise ValueError(f"La variable {expr.nombre} no tiene el atributo {expr.atributo}")
                return contexto[expr.nombre].atributos[expr.atributo]
            else:
                return contexto[expr.nombre]
            
        elif isinstance(expr,func):
            variables = expr.args
            parametros = []


            for var in variables:
                if isinstance(var,Variable):
                    if var.nombre not in contexto:
                        raise ValueError(f"No se ha econtrado la variable {var} en el contexto")
                    if var.atributo is not None : 
                        if var.atributo not  in contexto[var.nombre].atributos:
                            raise ValueError(f"No se ha econtrado el atributo {var.atributo} en la variable {var}")
                        parametros.append(contexto[var.nombre].atributos[var.atributo])
                    else:
                        parametros.append(contexto[var.nombre])
                elif isinstance(var,func) :
                    #Se podria refactorizar
                    parametros_funcion = []
                    args = var.args or []
                    for arg in args:
                        if isinstance(arg,Variable):
                            if arg.nombre not in contexto: 
                                raise ValueError(f"No se ha econtrado la variable {arg} en el contexto")
                            if arg.atributo is not None : 
                                if arg.atributo not  in contexto[arg.nombre].atributo:
                                    raise ValueError(f"No se ha econtrado el atributo {arg.atributo} en la variable {arg}")
                                parametros_funcion.append(contexto[arg.nombre].atributos[arg.atributo])
                            else:
                                parametros_funcion.append(contexto[arg.nombre])
                        else:
                            parametros_funcion.append(arg)

                    parametros.append(var.run(*args))
                else:
                    parametros.append(var)
            parametros = tuple(parametros)

            return expr.run(*parametros)

        else:
            #Se considera que es un tipo basico
            return expr

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
        logger.debug(f"[Condicion Comparacion] {val_izq} {self.comparador.value} {val_der} -> {resultado}")
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
            logger.debug(f"[Condicion Logica AND] Validando condiciones con AND")
            resultado = all(condicion.validar(contexto, base) for condicion in self.condiciones)
            #logger.debug(f"[Condicion Logica AND] Resultado AND -> {resultado}")
        elif self.operador == "OR":
            logger.debug(f"[Condicion Logica OR] Validando condiciones con OR")
            resultado = any(condicion.validar(contexto, base) for condicion in self.condiciones)
            #logger.debug(f"[Condicion Logica OR] Resultado OR -> {resultado}")
        else:
            raise ValueError(f"Operador lógico '{self.operador}' no reconocido")
        #en principio no hay condicion NOT aqui, ya hay una condicion negacion
        logger.debug(f"[Condicion Logica NOT] Resultado {self.operador} -> {resultado}")
        return resultado
    
class CondicionNegacion(Condicion):
    def __init__(self, condicion: Condicion):
        super().__init__(condicion.variables)
        self.condicion = condicion

    def validar(self, contexto: Dict[str, str], base: BaseConocimiento) -> bool:
        logger.debug(f"[Condicion Negacion] Validando condición de negación")
        resultado = not self.condicion.validar(contexto, base)
        #logger.debug(f"[Condicion Negacion] Resultado NOT -> {resultado}")
        return resultado
    
class CondicionAsignacion(Condicion):
    def __init__(self, variables: List, valiable_asignacion, valor):
        super().__init__(variables)
        #valor puede ser el nombre de una proposicion o un objeto func
        self.variable_asignacion = valiable_asignacion#Nombre de la variable donde se guardará la asignación
        self.asignacion = []# Lista donde se guardarán las tuplas que coincidan con la proposición
        self.nombre_proposicion = None
        self.funcion = None
        self.valor = None
        if isinstance(valor,str):
            self.nombre_proposicion = valor
        elif isinstance(valor,func):
            self.funcion = valor
        else:
            self.valor = valor
    def validar(self, contexto: Dict[str, str], base: BaseConocimiento) -> bool:
        if self.nombre_proposicion and self.valor ==None and self.nombre_proposicion not in base.proposiciones:
            raise ValueError(f"Proposición '{self.nombre_proposicion}' no existe")
        

        parametros = []

        #CUIDADO!!! Puede haber casos en los que no se tenga que reiniciar la asignacion. Por ejemplo si hay una variable multiple en la condicion.
        #self.asignacion = [] #hay que reiniciar la asignación cada vez que se valida la condición
        #Si es una variable, se sustituye por su valor en el contexto
        #Si no, se deja como está, puede ser un valor literal o individuo
        
        #for v in self.variables:
        #    if v not in contexto:
        #        parametros.append(v)
        #    else: 
        #        parametros.append(contexto[v])

        for var in self.variables:
            if isinstance(var,Variable):
                if var.nombre not in contexto:
                    raise ValueError(f"No se ha econtrado la variable {var} en el contexto")
                if var.atributo is not None : 
                    if var.atributo not  in contexto[var.nombre].atributos:
                        raise ValueError(f"No se ha econtrado el atributo {var.atributo} en la variable {var}")
                    parametros.append(contexto[var.nombre].atributos[var.atributo])
                else:
                    parametros.append(contexto[var.nombre])
            elif isinstance(var,func) :
                #Se podria refactorizar
                parametros_funcion = []
                args = var.args or []
                for arg in args:
                    if isinstance(arg,Variable):
                        if arg.nombre not in contexto: 
                           raise ValueError(f"No se ha econtrado la variable {arg} en el contexto")
                        if arg.atributo is not None : 
                            if arg.atributo not  in contexto[arg.nombre].atributo:
                                raise ValueError(f"No se ha econtrado el atributo {arg.atributo} en la variable {arg}")
                            parametros_funcion.append(contexto[arg.nombre].atributos[arg.atributo])
                        else:
                            parametros_funcion.append(contexto[arg.nombre])
                    else:
                        parametros_funcion.append(arg)
                parametros.append(var.run(*args))
            else:
                parametros.append(var)
        #Se debe de recorrer cada elemento de la proposicion, si los valores coinciden, se asigna el valor de la variable de asignación

        if self.nombre_proposicion is not None and self.valor is None:

            proposicion = base.proposiciones[self.nombre_proposicion]
            if not proposicion.elementos:
                logger.debug(f"[Condicion Asignacion] No hay elementos en la proposición {self.nombre_proposicion}")
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
                logger.debug(f"[Condicion Asignacion] No se encontraron coincidencias para la asignación")
                return False
            logger.debug(f"[Condicion Asignacion] Validación de asignación para {self.nombre_proposicion} con valores {parametros} y resultado {self.asignacion}")
            return True
        elif self.funcion is not None:
            parametros = tuple(parametros)
            elemento = self.funcion.run(*parametros)
            if elemento:
                self.asignacion.append(elemento)
                return True
            return False
        elif self.valor is not None:
            if isinstance(self.valor,Variable):
                self.asignacion.append(parametros[0])#Como es una variable se supone un unico valor
            else:
                self.asignacion.append(self.valor)
            return True
        else:
            raise ValueError(f"El valor de la asignacion no es un predicado o una funcion")


class CondicionRule(Condicion):
    def __init__(self,  nombre_regla: str,variables,motor):
        super().__init__(variables)
        self.nombre_regla = nombre_regla
        self.motor = motor

    def validar(self, contexto: Dict, base: BaseConocimiento) -> bool:

        parametros = []

        for variable in self.variables:


            if isinstance(variable,Variable):
                if variable.nombre not in contexto:
                    raise ValueError(f"La varaible {variable.nobmre} no esta en el contexto")
                if variable.atributo is not None:
                    if variable.atributo not in contexto[variable.nombre].atributos:
                        raise ValueError(f"La variable {variable.nobmre} no tiene el atributo {variable.atributo}")
                    parametros.append(contexto[variable.nombre].atributos[variable.atributo])
                else:
                    parametros.append(contexto[variable.nombre])
            elif isinstance(variable,func) :
                #Se podria refactorizar
                parametros_funcion = []
                args = variable.args or []
                for arg in args:
                    if isinstance(arg,Variable):
                        if arg.nombre not in contexto: 
                           raise ValueError(f"No se ha econtrado la variable {arg} en el contexto")
                        if arg.atributo is not None : 
                            if arg.atributo not  in contexto[arg.nombre].atributo:
                                raise ValueError(f"No se ha econtrado el atributo {arg.atributo} en la variable {arg}")
                            parametros_funcion.append(contexto[arg.nombre].atributos[arg.atributo])
                        else:
                            parametros_funcion.append(contexto[arg.nombre])
                    else:
                        parametros_funcion.append(arg)
                parametros.append(variable.run(*args))
            else:
                #Se considera que es un tipo basico
                parametros.append(variable)
                

        resultado = False
        regla = None
        try: 

            regla = self.motor.get_regla(self.nombre_regla)
            return regla.ejecutar(parametros, self.motor.base)
        except KeyError:
            raise ValueError(f"No se ha encontrado la regla {self.nombre_regla}")


        return resultado
