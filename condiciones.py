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
    def _df():
        pass
    def __init__(self, condiciones: List[Condicion], operador: str):
        super().__init__([])
        self.condiciones = condiciones
        self.operador = operador
        for condicion in condiciones:
            for var_condicion in condicion.variables:
                if var_condicion not in self.variables:
                    self.variables.append(var_condicion)
    def _validarCondicion(self,condiciones,contexto,base):
        oks = []
        for cond in self.condiciones:
            ok = False
            if isinstance(cond,CondicionLogica):
                #Las condiciones logicas manejan su propios contextos
                if cond.validar(contexto,base):
                    ok = True
                    logger.debug(f"[Regla:{self.nombre}:Condicion {indice}] Resultado condición '{type(cond).__name__}': {ok}")
                if not ok:
                    #logger.warning(f"[Regla:{self.nombre}] FALLA en contexto {contexto}")
                    return False , contexto
                indice +=1

            #obtenemos el contexto local, que es un subconjunto del contexto original, pero con las variables de la condición
            variables_cond = {}
            for var in cond.variables:
                if isinstance(var,Variable):
                    variables_cond[var.nombre]=var
            #variables_cond = list(variables_cond)


            contexto_local = {}
            for var in variables_cond.values():
                if var.nombre in contexto:
                    # Si la variable está en el contexto, se añade al contexto local
                    contexto_local[var.nombre] = contexto[var.nombre]
                #else:
                    # Si no está en el contexto, se deja tal cual
                    #contexto_local[var] = var
            #contexto_local = {var: contexto[var] for var in variables_cond if var in variables_cond}



            #comprobar si hay mas de una variable multiple
            var_mul = None
            contextos_locales = []#Cambiar nombre por contextos_locales
            for key in contexto_local.keys():
                if isinstance(contexto_local[key], list) and len(contexto_local[key]) > 1 and variables_cond[key].agregacion == False: #Si es una variables de agregacion, no se considera como variable multiple
                    if var_mul is not None:
                        raise ValueError(f"Más de una variable múltiple en el contexto: {var_mul} y {key}")
                    var_mul = key
            if var_mul is not None:
                #Si hay una variable multiple se debe hacer un contexto local por cada valor de la variable multiple
                valores_var_mul = contexto_local[var_mul]
                
                for valor in valores_var_mul:
                    #El contexto local no es un diccionario de listas, sino un diccionario de valores, por lo que se debe crear un nuevo contexto local con el valor de la variable multiple
                    #El contexto local es el contexto original sin la variable multiple
                    contexto_local_aux = {}

                    for k, v in contexto_local.items():
                        if k != var_mul: 
                            if  variables_cond[k].agregacion == False:       
                                contexto_local_aux[k] = v[0] 
                            else:#Si es una variable de agregación, se mantiene como lista
                                contexto_local_aux[k] = v
                    contexto_local_aux[var_mul] = valor
                    contextos_locales.append(contexto_local_aux)
            else:
                #Si no hay variable multiple, el contexto local es igual al contexto original pero sin listas, a no ser que sea una variable marcada como multiagregacion
                #El contexto local es el contexto original sin listas
                #nuevo_contexto = {}
                for k in list(contexto_local.keys()):
                    if variables_cond[k].agregacion==False:
                        contexto_local[k] = contexto_local[k][0]
                    else:
                        contexto_local[k] = contexto_local[k]
                #contexto_local = {k: v[0] for k, v in contexto_local.items()}
                contextos_locales.append(contexto_local)


            #Recorrer cada contexto local y validar la condición, si algun contexto local falla, se debe eliminar el valor de la variable multiple del contexto original si hay una variable multiple.
            for contexto_local in contextos_locales:
                if isinstance(cond, CondicionAsignacion):
                    #Se debe reiniciar la asignación de la condición,
                    cond.asignacion = []  # Reiniciar la asignación para cada contexto local
                    #Si la variable esta en el contexto habra que eliminarla antes????


                if cond.validar(contexto_local, base):
                    ok = True

                else:
                    #logger.debug(f"[Regla:{self.nombre}:Condicion {indice}] FALLA en contexto local {contexto_local} para condición {type(cond).__name__}")
                    if var_mul is not None:
                        #Si falla, se elimina el valor de la variable multiple del contexto original
                        contexto[var_mul].remove(contexto_local[var_mul])#Recuerda que contexto[var_mul] es una lista



            #Si la condicion es de tipo CondicionAsignacion, se debe comprobar que la asignación se ha realizado correctamente
            if isinstance(cond, CondicionAsignacion):
                if not cond.asignacion:
                    #logger.debug(f"[Regla:{self.nombre}:Condicion {indice}] No se encontraron coincidencias para la asignación en contexto {contexto_local}")
                    
                    
                    ok = False
                    #return False , contexto
                else:
                    #Si la asignación se ha realizado correctamente, se debe añadir al contexto
                    contexto[cond.variable_asignacion] = []#si no se ha inicializado, se inicializa como una lista vacía. Si ya existe, vacia igualmente
                    contexto[cond.variable_asignacion].extend(cond.asignacion)
                

            #logger.debug(f"[Regla:{self.nombre}:Condicion {indice}] Resultado condición '{type(cond).__name__}': {ok}")
            if not ok and self.operador =="AND" :
                #logger.warning(f"[Regla:{self.nombre}] FALLA en contexto {contexto}")
                return False , contexto
            elif ok and self.operador =="OR":
                return True,contexto
            #oks.append(ok)
        #logger.info(f"[Regla:{self.nombre}] VALIDADA correctamente para {contexto}")

        return ok , contexto



    def validar(self, contexto: Dict[str, str], base: BaseConocimiento) -> bool:
        if self.operador == "AND":
            logger.debug(f"[Condicion Logica AND] Validando condiciones con AND")
            resultado = self._validarCondicion(self.condiciones,contexto, base)
            #logger.debug(f"[Condicion Logica AND] Resultado AND -> {resultado}")
        elif self.operador == "OR":
            logger.debug(f"[Condicion Logica OR] Validando condiciones con OR")
            resultado = self._validarCondicion(self.condiciones,contexto, base) 
            #logger.debug(f"[Condicion Logica OR] Resultado OR -> {resultado}")
        else:
            raise ValueError(f"Operador lógico '{self.operador}' no reconocido")
        #en principio no hay condicion NOT aqui, ya hay una condicion negacion
        #logger.debug(f"[Condicion Logica NOT] Resultado {self.operador} -> {resultado}")
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
