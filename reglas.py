from typing import List
from itertools import product
import logging
from base import BaseConocimiento,Variable
logger = logging.getLogger("LOG")
from condiciones import Condicion, CondicionAsignacion
from consecuencias import Consecuencia


class Regla:
    def __init__(self, nombre: str, parametros: List[str], condiciones: List[Condicion], descripcion: str = None):
        self.nombre = nombre
        self.parametros = parametros
        self.condiciones = condiciones
        self.consecuencias: List[Consecuencia] = []
        self.descripcion = descripcion if descripcion else f"Proposición {nombre}: Sin descripción"

    def validar(self, valores: List[str], base: BaseConocimiento):
        #contexto = dict(zip(self.parametros, valores))
        contexto = {param: [valor] for param, valor in zip(self.parametros, valores)}
        #contexto = {}
        #for param, valor in zip(self.parametros, valores):
        #    contexto[param] =valor
        indice = 1
        logger.info(f"[Regla:{self.nombre}] Iniciar validación con contexto {contexto}")
        for cond in self.condiciones:


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
                if isinstance(contexto_local[key], list) and len(contexto_local[key]) > 1 and variables_cond[key].agregacion == False:
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
                            if  contexto_local_aux[k].agregacion == False:       
                                contexto_local_aux[k] = v[0] 
                            else:
                                contexto_local_aux[k] = v
                    contexto_local_aux[var_mul] = valor
                    contextos_locales.append(contexto_local_aux)
            else:
                #Si no hay variable multiple, el contexto local es igual al contexto original pero sin listas, a no ser que sea una variable marcada como multiagregacion
                #El contexto local es el contexto original sin listas
                nuevo_contexto = {}
                for k in list(contexto_local.keys()):
                    if variables_cond[k].agregacion==False:
                        contexto_local[k] = contexto_local[k][0]
                    else:
                        contexto_local[k] = contexto_local[k]
                #contexto_local = {k: v[0] for k, v in contexto_local.items()}
                contextos_locales.append(contexto_local)

            ok = False
            #Recorrer cada contexto local y validar la condición, si algun contexto local falla, se debe eliminar el valor de la variable multiple del contexto original si hay una variable multiple.
            for contexto_local in contextos_locales:
                if isinstance(cond, CondicionAsignacion):
                    #Se debe reiniciar la asignación de la condición,
                    cond.asignacion = []  # Reiniciar la asignación para cada contexto local

                if cond.validar(contexto_local, base):
                    ok = True

                else:
                    logger.debug(f"[Regla:{self.nombre}:Condicion {indice}] FALLA en contexto local {contexto_local} para condición {type(cond).__name__}")
                    if var_mul is not None:
                        #Si falla, se elimina el valor de la variable multiple del contexto original
                        contexto[var_mul].remove(contexto_local[var_mul])#Recuerda que contexto[var_mul] es una lista



            #Si la condicion es de tipo CondicionAsignacion, se debe comprobar que la asignación se ha realizado correctamente
            if isinstance(cond, CondicionAsignacion):
                if not cond.asignacion:
                    logger.debug(f"[Regla:{self.nombre}:Condicion {indice}] No se encontraron coincidencias para la asignación en contexto {contexto_local}")
                    return False , contexto
                else:
                    #Si la asignación se ha realizado correctamente, se debe añadir al contexto
                    contexto[cond.variable_asignacion] = []#si no se ha inicializado, se inicializa como una lista vacía. Si ya existe, vacia igualmente
                    contexto[cond.variable_asignacion].extend(cond.asignacion)
            

            logger.debug(f"[Regla:{self.nombre}:Condicion {indice}] Resultado condición '{type(cond).__name__}': {ok}")
            if not ok:
                #logger.warning(f"[Regla:{self.nombre}] FALLA en contexto {contexto}")
                return False , contexto
            indice +=1
        logger.info(f"[Regla:{self.nombre}] VALIDADA correctamente para {contexto}")
        return True , contexto

    def ejecutar(self, valores: List[str], base: BaseConocimiento):
        boolean , contexto = self.validar(valores, base)
        indice = 1 #Para informar en el loger de la posicion de la consecuencia
        if boolean:
            logger.info(f"[Regla:{self.nombre}] Ejecutando consecuencia en {valores}")
            #contexto = dict(zip(self.parametros, valores))
            for c in self.consecuencias:

                #Empiezo obteniendo las variables que se usaran en la consecuencia
                variables_cons = set()
                for var in c.variables:
                    if isinstance(var,Variable):
                        variables_cons.add(var.nombre)

                variables_cons = list(variables_cons)


                contexto_local = {}#El contexto local seran las variables y valores que se usaran en la consecuencia
                for var in variables_cons:
                    if var in contexto:
                        # Solo se añaden al contesto las variables que ya estaban en el contexto global
                        contexto_local[var] = contexto[var]
                    #Si una variable de la consecuencia no se añade al contexto, posiblemente saltara un error mas adelante. A no ser que sea algun tipo especial como '_'

                #Comprobamos si hay variables multiples. Solo se permite una variable multiple por consecuencia. Habra tantos contextos locales como variables multiples y se ejecuta la consecuencia el mismo numero de veces.
                var_mul = None
                contextos_locales = []
                for key in contexto_local.keys():
                    if isinstance(contexto_local[key], list) and len(contexto_local[key]) > 1:
                        if var_mul is not None:
                            raise ValueError(f"Más de una variable múltiple en el contexto: {var_mul} y {key}")
                        var_mul = key

                if var_mul is not None:
                    #Si hay una variable multiple se debe hacer un contexto local por cada valor de la variable multiple
                    valores_var_mul = contexto_local[var_mul]
                    
                    for valor in valores_var_mul:
                        #El contexto local no es un diccionario de listas, sino un diccionario de valores, por lo que se debe crear un nuevo contexto local con el valor de la variable multiple
                        contexto_local_aux = {k: v[0] for k, v in contexto_local.items() if k != var_mul}#El contexto local es el contexto original sin la variable multiple
                        contexto_local_aux[var_mul] = valor
                        contextos_locales.append(contexto_local_aux)
                else:
                    #Si no hay variable multiple, el contexto local es igual al contexto original pero sin listas
                    contexto_local = {k: v[0] for k, v in contexto_local.items()}#El contexto local es el contexto original sin listas
                    contextos_locales.append(contexto_local)

                for contx in contextos_locales:

                    c.ejecutar(contx, base)
            logger.info(f"[Regla:{self.nombre}] Consecuencias ejecutadas")
