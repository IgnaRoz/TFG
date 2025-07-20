from abc import ABC, abstractmethod
from typing import Dict, List, Tuple, Union

import logging
from base import BaseConocimiento, TipoOperacion,Variable
from func import func

logger = logging.getLogger("LOG")


def _sustituir_parametros(contexto,variables):
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
    #parametros = tuple(parametros)
    return parametros


class Consecuencia(ABC):
    def __init__(self, variables: List[str]):
        self.variables = variables

    @abstractmethod
    def ejecutar(self, contexto: Dict[str, str], base: BaseConocimiento):
        pass


class ConsecuenciaAsignacion(Consecuencia):
    def __init__(self, proposicion: str,  variables: List[str],atributos=None):
        super().__init__(variables)
        self.proposicion = proposicion
        self.atributos = atributos
        #self.parametros = parametros

    def ejecutar(self, contexto: Dict[str, str], base: BaseConocimiento):
        #tupla = tuple(contexto.get(p, p) for p in self.variables)
        if self.proposicion not in base.proposiciones:
            #No se debe permitir añadir elementos a una proposicion no registrada, ni crearse una nueva
            raise ValueError("No se ha econtrado la prposicion")
            #base.crear_proposicion(self.proposicion, len(tupla))

        parametros = []
        #Si es una variable, se sustituye por su valor en el contexto
        #Si no, se deja como está, puede ser un valor literal o individuo
        
        parametros = _sustituir_parametros(contexto,self.variables)

        #for variable in self.variables:
        #    if '.' in variable:
        #        var,atr = variable.split('.',1)
        #   
        #        if var in contexto:
        #            if atr not in contexto[var].atributos:
        #                raise ValueError(f"El atributo {atr} no esta en la variable {var}")
        #            param = contexto[var].atributos[atr]
        #            parametros.append(param)
        #            continue  
        #    else:
        #        if variable in contexto:
        #            parametros.append(contexto[variable])
        #            continue                  
        #    parametros.append(variable)


        #for i_contexto in contexto:
        #    
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
        #            #Si no es ni variable, ni atributo, entonces se considera un valor basico
        #            parametros.append(variable)
#

        tupla = tuple(parametros)

        #Falta sustituir paramteros en atributos
        atributos = self.atributos
        atributos_parametros = {}
        for atributo_nombre, atributo in atributos.items():
            if isinstance(atributo, Variable):
                if atributo.nombre not in contexto:
                    raise ValueError(f"No se ha econtrado la variable {atributo} en el contexto")
                if atributo.atributo is not None:
                    if atributo.atributo not in contexto[atributo.nombre].atributos:
                        raise ValueError(f"No se ha econtrado el atributo {atributo.atributo} en la variable {atributo}")
                    atributos_parametros[atributo_nombre] = contexto[atributo.nombre].atributos[atributo.atributo]
                else:
                    atributos_parametros[atributo_nombre] = contexto[atributo.nombre]
            else:
                atributos_parametros[atributo_nombre] = atributo

        try:
            base.proposiciones[self.proposicion].add(tupla,atributos_parametros)
            logger.info(f"[Accion] Add {tupla} to {self.proposicion}")
        except ValueError as e:
            logger.warning(e)

class ConsecuenciaEliminacion(Consecuencia):
    def __init__(self, proposicion: str,  variables: List[str]):
        super().__init__(variables)
        self.proposicion = proposicion
        #self.parametros = parametros

    def ejecutar(self, contexto: Dict[str, str], base: BaseConocimiento):
        tupla = tuple(contexto.get(p, p) for p in self.variables)
        if self.proposicion not in base.proposiciones:
            raise ValueError(f"Proposición '{self.proposicion}' no existe")
        
        parametros = []
    
        parametros = _sustituir_parametros(contexto,self.variables)
        tupla = tuple(parametros)

        base.proposiciones[self.proposicion].eliminar(tupla)
        logger.info(f"[Accion] Eliminar {tupla} de {self.proposicion}")

class ConsecuenciaFuncion(Consecuencia):
    def __init__(self, variables,funcion):
        super().__init__(variables)
        self.funcion = funcion

    def ejecutar(self,contexto,base):
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
        self.funcion.run(*parametros)


class ConsecuenciaModificacion(Consecuencia):
    def __init__(
        self,
        objetivo: Variable,
        #atributo: str,
        operacion: TipoOperacion,
        valor,
        #atributo_valor: str = None,
        variables: List[str] = None,
    ):
        super().__init__(variables or [])
        self.objetivo = objetivo
        #self.atributo = atributo
        self.operacion = operacion
        self.valor = valor
        #self.atributo_valor = atributo_valor

    def ejecutar(self, contexto: Dict[str, str], base: BaseConocimiento):
        
        #Hay que crear contextos locales y eliminar las listas de los contextos

        #De momento solo se coge el primer valor, por lo que no existen la multivariable en las consecuencias

        #variable = contexto.get(self.objetivo)[0]

        valor = None
        if isinstance(self.valor,Variable):
            if self.valor.nombre not in contexto:
                raise ValueError(f"La variable {self.valor.nombre} no se encuentra en el contexto")
            if self.valor.atributo is not None:
                if self.valor.atributo not in contexto[self.valor.nombre].atributos:
                    raise ValueError(f"No se encuentra el atributo {self.valor.atributo} en ka variable {self.valor.nombre}")
                valor = contexto[self.valor.nombre].atributos[self.valor.atributo]
            else:
                valor = contexto[self.valor.nombre]
        elif isinstance(self.valor,func):
            parametros =_sustituir_parametros(contexto,self.valor.args)
            parametros = tuple(parametros)
            valor = self.valor.run(*parametros)
        elif isinstance(self.valor,int):
            valor = self.valor
        elif isinstance(self.valor,str):
            valor = self.valor
        else:
            raise ValueError(f"Tipo de valor no reconocido")
        

        if self.objetivo.nombre not in contexto:
            raise ValueError(f"La variable objetivo {self.objetivo} no se encuentra en el contexto")
        if self.objetivo.atributo is not None and self.objetivo.atributo not in contexto[self.objetivo.nombre].atributos:
            raise ValueError(f"No se encuentra el atributo {self.objetivo.atributo} en la variable objetivo {self.objetivo}")

        variable_contexto=  contexto[self.objetivo.nombre]
        #elemento = base.proposiciones[variable_contexto.nombre_prop].elementos[variable_contexto.tupla]
        if self.operacion == TipoOperacion.ASIGNACION:
            if self.objetivo.atributo is not None:  
                variable_contexto.atributos[self.objetivo.atributo] = valor
            else: 
                contexto[self.objetivo.nombre] = valor
            #elemento.atributos[self.objetivo.atributo] = valor
        elif self.operacion == TipoOperacion.INCREMENTO:
            if self.objetivo.atributo is not None:  
                variable_contexto.atributos[self.objetivo.atributo] += valor
            else: 
                contexto[self.objetivo.nombre] += valor
             #elemento.atributos[self.objetivo.atributo] += valor
        elif self.operacion == TipoOperacion.DECREMENTO:
            if self.objetivo.atributo is not None:  
                variable_contexto.atributos[self.objetivo.atributo] -= valor
            else: 
                contexto[self.objetivo.nombre] -= valor
             #elemento.atributos[self.objetivo.atributo] -= valor
        return
        

        variable, atributo = self.objetivo.split('.',1)
        if '.' in atributo:
            raise ValueError("Un atributo no puede tener atributos")
        if variable in contexto:
            variable = contexto.get(variable)
        else:
            raise ValueError(f"No se ha econtrado econtrado la variable {variable} en el contexto")
        if atributo not in variable.atributos:
            raise ValueError(f"No se ha econtrado el atributo {atributo} para la variable {variable} en el contexto")
        valor = self.valor
        logger.info(f"[Accion] Modificar {variable}.{atributo} {self.operacion.value} {valor}")
        if self.operacion == TipoOperacion.ASIGNACION:
            variable.atributos[atributo] = valor
        elif self.operacion == TipoOperacion.INCREMENTO:
            variable.atributos[atributo] += valor
        elif self.operacion == TipoOperacion.DECREMENTO:
            variable.atributos[atributo] -= valor
        return

        id_ = contexto.get(self.objetivo, self.objetivo)
        indiv = base.individuos.obtener(id_)
        if indiv is None:
            raise ValueError(f"Individuo '{id_}' no existe")
        if self.atributo not in indiv:
            raise ValueError(f"Atributo '{self.atributo}' no existe en '{id_}'")
        if not isinstance(indiv[self.atributo], int):
            raise ValueError("El atributo debe ser de tipo entero para modificaciones")

        if isinstance(self.valor, tuple):
            id_valor = contexto.get(self.valor[0], self.valor[0])
            valor_real = base.individuos.obtener(id_valor)[self.valor[1]]
        elif isinstance(self.valor, str) and self.valor in contexto:
            id_valor = contexto[self.valor]
            valor_real = base.individuos.obtener(id_valor)[self.atributo_valor]
        else:
            valor_real = self.valor

        logger.info(f"[Accion] Modificar {id_}.{self.atributo} {self.operacion.value} {valor_real}")
        if self.operacion == TipoOperacion.ASIGNACION:
            indiv[self.atributo] = valor_real
        elif self.operacion == TipoOperacion.INCREMENTO:
            indiv[self.atributo] += valor_real
        elif self.operacion == TipoOperacion.DECREMENTO:
            indiv[self.atributo] -= valor_real


class ConsecuenciaRule(Consecuencia):
    def __init__(self, nombre_regla: str,  variables: List[str],motor):
        super().__init__(variables)
        self.nombre_regla = nombre_regla
        self.motor = motor


    def ejecutar(self, contexto: Dict[str, str], base: BaseConocimiento):

        parametros = []
        parametros = _sustituir_parametros(contexto,self.variables)

        tupla = tuple(parametros)
        try: 
            regla = self.motor.get_regla(self.nombre_regla)
            regla.ejecutar(tupla, self.motor.base)
        except KeyError:
            raise ValueError(f"No se ha encontrado la regla {self.nombre_regla}")
