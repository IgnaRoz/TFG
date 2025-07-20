import logging
from typing import Dict, Set, Tuple, List, Union
from enum import Enum
import operator
#from motorEjecucion import motor


class TipoComparacion(Enum):
    IGUAL = "=="
    DIFERENTE = "!="
    MAYOR = ">"
    MENOR = "<"
    MAYOR_IGUAL = ">="
    MENOR_IGUAL = "<="


class TipoOperacion(Enum):
    ASIGNACION = "="
    INCREMENTO = "+="
    DECREMENTO = "-="


OPERADORES = {
    TipoComparacion.IGUAL: operator.eq,
    TipoComparacion.DIFERENTE: operator.ne,
    TipoComparacion.MAYOR: operator.gt,
    TipoComparacion.MENOR: operator.lt,
    TipoComparacion.MAYOR_IGUAL: operator.ge,
    TipoComparacion.MENOR_IGUAL: operator.le,
}

class Variable():
    def __init__(self,nombre,atributo=None,agregacion = False):
        self.nombre = nombre
        self.atributo = atributo
        self.agregacion = agregacion

class Individuos:#Borrar, no es necesario
    def __init__(self):
        self.individuos: Dict[str, Dict[str, Union[str, int, bool]]] = {}

    def registrar(self, id_: str, atributos: Dict[str, Union[str, int, bool]]):
        if id_ not in self.individuos:
            self.individuos[id_] = atributos
        else:
            self.individuos[id_].update(atributos)

    def obtener(self, id_: str) -> Dict[str, Union[str, int, bool]]:
        return self.individuos.get(id_)


class Proposicion:
    def __init__(self, nombre: str, parametros:List[str],descripcion: str = None,atributos = None ,padre = None,atributos_defecto = None):#Hay que incluir el nombre de los parametros
        self.nombre = nombre
        self.n = len(parametros)
        self.padre = padre
        self.parametros = parametros
        self.elementos = {}
        self.descripcion = descripcion if descripcion else f"Sin descripción"
        if atributos:
            self.atributos = atributos
        else:
            self.atributos = []
        if atributos_defecto:
            self.atributos_defecto =atributos_defecto
        else:
            self.atributos_defecto ={}


        p = padre
        while p:#mientras exista un padre, se le va añadiendo mas atributos heredados
            #if not p.atributos:
            #    p = p.padre
            #    continue
            for atributo in p.atributos:
                if atributo not in self.atributos:
                    self.atributos.append(atributo)
                else:
                    raise ValueError(f"El atributo {atributo} ya esta asignado mediante herencia por {p.nombre}")
                
            for atributo,valor in p.atributos_defecto.items():
                #Si el padre tiene un atributo por defecto que el hijo no tiene, entonces se hereda el valor
                if atributo not in self.atributos_defecto:
                    self.atributos_defecto[atributo] = valor
                #Si atributo por defecto del padre esta ya añadido como atributo por defecto, no se sustituye. Prevalece el de menor jerarquia
            p = p.padre
        
    def add(self, tupla: Tuple[str, ...],atributos =None):
        if len(tupla) != self.n :
            raise ValueError(f"Todas las tuplas deben tener {self.n} individuos")
        if tupla in self.elementos.keys():
            raise ValueError(f"La tupla {tupla} ya existe en {self.nombre}")

        
        atributos = {} if not atributos else atributos
        
        #vamos a exigir todos los atributos, a no ser que sean atributos por defectos
        for nombre_atributo in self.atributos:
            
            if not nombre_atributo in self.atributos_defecto and not nombre_atributo in atributos.keys() :
                raise ValueError(f"La proposicion{self.nombre} necesita el atributo {nombre_atributo}")

        #Tambien vamos a exigir es que no se añadan atributos nuevos
        for atributo in atributos:
            if atributo not in self.atributos:
                raise ValueError(f"La proposicion {self.nombre} no tiene el atributo {atributo}")
    
        for i,parametro in enumerate(self.parametros):
            atributos[parametro] = tupla[i]
        for atributo,valor in self.atributos_defecto.items():
            if atributo not in atributos:
                atributos[atributo] = valor

        elemento = ElementoProposicion(self.nombre,self, tupla,atributos)
        self.elementos[tupla] = elemento  

        #Un elemento con herenecia tambien pertenece a la proposicion padre.
        padre = self.padre
        while padre:
            padre.elementos[tupla] = elemento
            logging.getLogger("LOG").debug(f"[{padre.nombre}] Added tuple {elemento.tupla} with attributes {elemento.atributos}")
            padre = padre.padre

        #self.tuplas.add(tupla)
        return elemento

    def eliminar(self, tupla: Tuple[str, ...]):

        #Cuando se elimina una proposicion y esta tiene herencia, se elimina de todas empezando por la original
        if not self.existe(tupla):
            raise ValueError(f"La tupla {tupla} no existe en {self.nombre}")
        #Eliminacion en cascada desde el origen
        padre = self.elementos[tupla].proposicion
        while padre:
            padre.elementos.pop(tupla)
            logging.getLogger("LOG").debug(f"[{padre.nombre}] Eliminada tupla {tupla}")
            padre = padre.padre
        

        #if tupla not in self.elementos.keys():
        #    raise ValueError(f"La tupla {tupla} no existe en {self.nombre}")
        #self.elementos.pop(tupla)
        #logging.getLogger("LOG").debug(f"[{self.nombre}] Eliminada tupla {tupla}")

    def existe(self, tupla: Tuple[str, ...]) -> bool:
        for elemento in self.elementos.values():
            coincide = True
            for i, param in enumerate(tupla):
                if param not in ("_", "") and elemento.tupla[i] != param:
                    coincide = False
                    break
            if coincide:
                return elemento
        return tupla in self.elementos
class ElementoProposicion:
    def __init__(self, nombre_prop: str,proposicion:Proposicion, tupla,atributos):
        self.nombre_prop = nombre_prop
        self.proposicion = proposicion
        self.tupla = tupla
        self.atributos = atributos 
    def __str__(self):
        # Formatea la tupla sin espacios: "(1,2,3)"
        tupla_str = "(" + ",".join(str(x) for x in self.tupla) + ")"
        # Formatea los atributos como "clave1:valor1,clave2:valor2"
        attrs_str = ",".join(f"{k}:{v}" for k, v in self.atributos.items())
        return f"{self.nombre_prop}{tupla_str}{{{attrs_str}}}"
    def __repr__(self):
        return self.__str__()

class Categoria:
    def __init__(self, nombre: str, esquema: Dict[str, type]):
        for tipo in esquema.values():
            if tipo not in (str, int, bool):
                raise ValueError("Solo se permiten tipos str, int o bool")
        self.nombre = nombre
        self.esquema = esquema


class BaseConocimiento:
    def __init__(self):
        self.individuos = Individuos()#Borrar
        self.categorias: Dict[str, Categoria] = {}#Borrar
        self.proposiciones: Dict[str, Proposicion] = {}

    #Borrar
    def crear_categoria(self, nombre: str, esquema: Dict[str, type]):
        if nombre in self.categorias:
            raise ValueError(f"La categoría '{nombre}' ya existe")
        self.categorias[nombre] = Categoria(nombre, esquema)
        self.proposiciones[nombre] = Proposicion(nombre, 1)

    def crear_proposicion(self, nombre: str, parametros: List[str],descripcion: str = None,atributos:Dict =None,padre=None,atributos_defecto = None):
        if nombre in self.proposiciones:
            raise ValueError(f"La proposición '{nombre}' ya existe")
        self.proposiciones[nombre] = Proposicion(nombre, parametros,descripcion,atributos=atributos,padre= padre,atributos_defecto=atributos_defecto)#Añadir luego parametros y atributos

    #Borrar
    def asignar_individuo_a_categoria(
        self, id_: str, categoria: str, atributos: Dict[str, Union[str, int, bool]]
    ):
        if categoria not in self.categorias:
            raise ValueError(f"La categoría '{categoria}' no existe")
        cat = self.categorias[categoria]
        for clave, valor in atributos.items():
            if clave not in cat.esquema or not isinstance(valor, cat.esquema[clave]):
                raise ValueError(f"Atributo {clave} inválido para la categoría {categoria}")
        self.individuos.registrar(id_, atributos)
        if self.proposiciones[categoria].existe((id_,)):
            raise ValueError(f"El individuo '{id_}' ya está en la categoría '{categoria}'")
        self.proposiciones[categoria].add((id_,))
