import logging
from typing import Dict, Set, Tuple, List, Union
from enum import Enum
import operator


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

class Individuos:
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
    def __init__(self, nombre: str, parametros:List[str],descripcion: str = None,atributos = None ):#Hay que incluir el nombre de los parametros
        self.nombre = nombre
        self.n = len(parametros)
        self.parametros = parametros
        self.elementos = {}
        self.descripcion = descripcion if descripcion else f"Sin descripción"
        if atributos:
            self.atributos = atributos
        else:
            self.atributos = []
        
    def add(self, tupla: Tuple[str, ...],atributos =None):
        if len(tupla) != self.n :
            raise ValueError(f"Todas las tuplas deben tener {self.n} individuos")
        if tupla in self.elementos.keys():
            raise ValueError(f"La tupla {tupla} ya existe en {self.nombre}")

        
        atributos = {} if not atributos else atributos
        
        #vamos a exigir todos los atributos
        for nombre_atributo in self.atributos:
            
            if not nombre_atributo in atributos.keys():
                raise ValueError(f"La proposicion{self.nombre} necesita el atributo {nombre_atributo}")

        #Tambien vamos a exigir es que no se añadan atributos nuevos
        for atributo in atributos:
            if atributo not in self.atributos:
                raise ValueError(f"La proposicion {self.nombre} no tiene el atributo {atributo}")

        for i,parametro in enumerate(self.parametros):
            atributos[parametro] = tupla[i]

        elemento = ElementoProposicion(self.nombre, tupla,atributos)
        self.elementos[tupla] = elemento  

        #self.tuplas.add(tupla)
        logging.getLogger("LOG").debug(f"[{self.nombre}] Added tuple {elemento.tupla} with attributes {elemento.atributos}")
        return elemento

    def eliminar(self, tupla: Tuple[str, ...]):
        if tupla not in self.elementos.keys():
            raise ValueError(f"La tupla {tupla} no existe en {self.nombre}")
        self.elementos.pop(tupla)
        logging.getLogger("LOG").debug(f"[{self.nombre}] Eliminada tupla {tupla}")

    def existe(self, tupla: Tuple[str, ...]) -> bool:
        return tupla in self.elementos
class ElementoProposicion:
    def __init__(self, nombre_prop: str, tupla,atributos):
        self.nombre_prop = nombre_prop
        self.tupla = tupla
        self.atributos = atributos 



class Categoria:
    def __init__(self, nombre: str, esquema: Dict[str, type]):
        for tipo in esquema.values():
            if tipo not in (str, int, bool):
                raise ValueError("Solo se permiten tipos str, int o bool")
        self.nombre = nombre
        self.esquema = esquema


class BaseConocimiento:
    def __init__(self):
        self.individuos = Individuos()
        self.categorias: Dict[str, Categoria] = {}
        self.proposiciones: Dict[str, Proposicion] = {}

    def crear_categoria(self, nombre: str, esquema: Dict[str, type]):
        if nombre in self.categorias:
            raise ValueError(f"La categoría '{nombre}' ya existe")
        self.categorias[nombre] = Categoria(nombre, esquema)
        self.proposiciones[nombre] = Proposicion(nombre, 1)

    def crear_proposicion(self, nombre: str, parametros: List[str],descripcion: str = None,atributos:Dict =None):
        if nombre in self.proposiciones:
            raise ValueError(f"La proposición '{nombre}' ya existe")
        self.proposiciones[nombre] = Proposicion(nombre, parametros,descripcion,atributos=atributos)#Añadir luego parametros y atributos

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
