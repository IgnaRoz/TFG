from typing import List
from itertools import product
import logging
from base import BaseConocimiento,Variable
logger = logging.getLogger("LOG")
from condiciones import Condicion, CondicionAsignacion, CondicionFuncion,CondicionLogica
from consecuencias import Consecuencia, ConsecuenciaAsignacion, ConsecuenciaModificacion


class Regla:
    def __init__(self, nombre: str, parametros: List[str], condiciones: List[Condicion], descripcion: str = None):
        self.nombre = nombre
        self.parametros = parametros
        self.condiciones = condiciones
        self.consecuencias: List[Consecuencia] = []
        self.descripcion = descripcion if descripcion else f"Proposición {nombre}: Sin descripción"
        self.contingencias =[]

    def validar(self, valores: List[str], base: BaseConocimiento):
        #contexto = dict(zip(self.parametros, valores))
        contexto ={}
        if isinstance(self,Contingencia) and not self.precondicion: 
            #Si es una contingencia de precondicion no se debe de tomar los valores como contexto, porque no inicializa los parametros iniciales
            contexto = valores
        else:

            contexto = {param: [valor] for param, valor in zip(self.parametros, valores)}
        #contexto = {}
        #for param, valor in zip(self.parametros, valores):
        #    contexto[param] =valor
        indice = 1
        logger.info(f"[Regla:{self.nombre}] Iniciar validación con contexto {contexto}")
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
                continue
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
                            if  contexto_local_aux[k].agregacion == False:       
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

        #Antes de validar las condiciones se comprueba si hay contingencias precondiciones
        for contingencia in self.contingencias:
            if not isinstance(contingencia,Contingencia) or contingencia.precondicion != True:
                #No es una contingencia de precondicion y se salta
                continue
            contingencia.ejecutar(valores,base)
            

        boolean , contexto = self.validar(valores, base)
        #Despues de validar las condiciones se comprueba si hay contingencias 
        for contingencia in self.contingencias:
            if not isinstance(contingencia,Contingencia) or contingencia.precondicion != False or contingencia.posconsecuencia != False:
                #No es una contingencia de precondicion y se salta
                continue
            contingencia.ejecutar(contexto,base)


        indice = 1 #Para informar en el loger de la posicion de la consecuencia
        if boolean:
            logger.info(f"[Regla:{self.nombre}] Ejecutando consecuencia en {valores}")
            #contexto = dict(zip(self.parametros, valores))
            for c in self.consecuencias:

                #Empiezo obteniendo las variables que se usaran en la consecuencia
                variables_cons = {}
                for var in c.variables:
                    if isinstance(var,Variable):
                        variables_cons[var.nombre]=var
                if isinstance(c,ConsecuenciaAsignacion):
                    for atributo in c.atributos:
                        if isinstance(c.atributos[atributo],Variable):
                            variables_cons[c.atributos[atributo].nombre] = c.atributos[atributo]
                    #if c.

                #variables_cons = list(variables_cons)


                contexto_local = {}#El contexto local seran las variables y valores que se usaran en la consecuencia
                for var in variables_cons.values():
                    if var.nombre in contexto:
                        # Solo se añaden al contesto las variables que ya estaban en el contexto global
                        contexto_local[var.nombre] = contexto[var.nombre]
                    #Si una variable de la consecuencia no se añade al contexto, posiblemente saltara un error mas adelante. A no ser que sea algun tipo especial como '_'

                #Comprobamos si hay variables multiples. Solo se permite una variable multiple por consecuencia. Habra tantos contextos locales como variables multiples y se ejecuta la consecuencia el mismo numero de veces.
                var_mul = None
                contextos_locales = []
                for key in contexto_local.keys():
                    if isinstance(contexto_local[key], list) and len(contexto_local[key]) > 1 and variables_cons[key].agregacion == False:
                        if var_mul is not None:
                            raise ValueError(f"Más de una variable múltiple en el contexto: {var_mul} y {key}")
                        var_mul = key

                if var_mul is not None:
                    #Si hay una variable multiple se debe hacer un contexto local por cada valor de la variable multiple
                    valores_var_mul = contexto_local[var_mul]
                    
                    for valor in valores_var_mul:
                        #El contexto local no es un diccionario de listas, sino un diccionario de valores, por lo que se debe crear un nuevo contexto local con el valor de la variable multiple
                        contexto_local_aux = {}
                        for k, v in contexto_local.items():
                            if k != var_mul: 
                                if  variables_cons[k].agregacion == False:       
                                    contexto_local_aux[k] = v[0] 
                                else:#Si es una variable de agregación, se mantiene como lista
                                    contexto_local_aux[k] = v

                        contexto_local_aux[var_mul] = valor
                        contextos_locales.append(contexto_local_aux)
                else:
                    #Si no hay variable multiple, el contexto local es igual al contexto original pero sin listas
                    
                    #nuevo_contexto = {}
                    for k in list(contexto_local.keys()):
                        if variables_cons[k].agregacion==False:
                            contexto_local[k] = contexto_local[k][0]
                        else:
                            contexto_local[k] = contexto_local[k]
                            
                    #contexto_local = {k: v[0] for k, v in contexto_local.items()}#El contexto local es el contexto original sin listas
                    contextos_locales.append(contexto_local)

                for contx in contextos_locales:

                    c.ejecutar(contx, base)
                    if isinstance(c,ConsecuenciaModificacion):
                        contexto[c.objetivo.nombre] = [contx[c.objetivo.nombre]]
            logger.info(f"[Regla:{self.nombre}] Consecuencias ejecutadas")


            for contingencia in self.contingencias:
                if not isinstance(contingencia,Contingencia) or contingencia.posconsecuencia != True:
                    #No es una contingencia de precondicion y se salta
                    continue
                contingencia.ejecutar(contexto,base)
            return True #Si la regla es validad correctamente y ejecuta las consecuencias, la regla devuelve True
        return False #De lo contrario devuelve False


class Contingencia(Regla):
    def __init__(self, nombre: str, parametros: List[str], condiciones: List[Condicion], descripcion: str = None,precondicion: bool = False,posconsecuencia: bool = False):
  
        super().__init__(nombre, parametros, condiciones, descripcion)
        self.precondicion = precondicion
        self.posconsecuencia = posconsecuencia
        