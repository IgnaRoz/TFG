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
    def __init__(self, nombre: str, n: int):
        self.nombre = nombre
        self.n = n
        self.tuplas: Set[Tuple[str, ...]] = set()

    def add(self, tupla: Tuple[str, ...]):
        if len(tupla) != self.n:
            raise ValueError(f"Todas las tuplas deben tener {self.n} individuos")
        if tupla in self.tuplas:
            raise ValueError(f"La tupla {tupla} ya existe en {self.nombre}")
        self.tuplas.add(tupla)
        logging.getLogger("LOG").debug(f"[{self.nombre}] Added tuple {tupla}")

    def eliminar(self, tupla: Tuple[str, ...]):
        if tupla not in self.tuplas:
            raise ValueError(f"La tupla {tupla} no existe en {self.nombre}")
        self.tuplas.discard(tupla)
        logging.getLogger("LOG").debug(f"[{self.nombre}] Eliminada tupla {tupla}")

    def existe(self, tupla: Tuple[str, ...]) -> bool:
        return tupla in self.tuplas


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

    def crear_proposicion(self, nombre: str, n: int):
        if nombre in self.proposiciones:
            raise ValueError(f"La proposición '{nombre}' ya existe")
        self.proposiciones[nombre] = Proposicion(nombre, n)

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
