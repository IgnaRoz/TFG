import logging
from typing import Dict, Set, Tuple, List, Union
from enum import Enum
import operator


class LogColors:
    DEBUG = "\033[94m"
    INFO = "\033[92m"
    WARNING = "\033[93m"
    ERROR = "\033[91m"
    RESET = "\033[0m"


class ColoredFormatter(logging.Formatter):
    LEVEL_COLOR = {
        'DEBUG': LogColors.DEBUG,
        'INFO': LogColors.INFO,
        'WARNING': LogColors.WARNING,
        'ERROR': LogColors.ERROR,
        'CRITICAL': LogColors.ERROR,
    }

    def format(self, record):
        color = self.LEVEL_COLOR.get(record.levelname, LogColors.RESET)
        message = super().format(record)
        return f"{color}{message}{LogColors.RESET}"


handler = logging.StreamHandler()
handler.setFormatter(
    ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.handlers = [handler]


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
        self.tuplas.add(tupla)
        logger.debug(f"[{self.nombre}] Added tuple {tupla}")

    def eliminar(self, tupla: Tuple[str, ...]):
        self.tuplas.discard(tupla)
        logger.debug(f"[{self.nombre}] Eliminada tupla {tupla}")

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
        self.categorias[nombre] = Categoria(nombre, esquema)
        self.proposiciones[nombre] = Proposicion(nombre, 1)

    def crear_proposicion(self, nombre: str, n: int):
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
        self.proposiciones[categoria].add((id_,))
