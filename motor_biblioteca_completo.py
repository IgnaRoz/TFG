import logging
from typing import Dict, Set, Tuple, List, Union
from enum import Enum
from abc import ABC, abstractmethod
import operator

# Colores ANSI para logs
class LogColors:
    DEBUG = "\033[94m"      # Azul claro
    INFO = "\033[92m"       # Verde
    WARNING = "\033[93m"    # Amarillo
    ERROR = "\033[91m"      # Rojo
    RESET = "\033[0m"

# Configuración del logger con timestamp, nivel y colores
class ColoredFormatter(logging.Formatter):
    LEVEL_COLOR = {
        'DEBUG': LogColors.DEBUG,
        'INFO': LogColors.INFO,
        'WARNING': LogColors.WARNING,
        'ERROR': LogColors.ERROR,
        'CRITICAL': LogColors.ERROR
    }

    def format(self, record):
        color = self.LEVEL_COLOR.get(record.levelname, LogColors.RESET)
        message = super().format(record)
        return f"{color}{message}{LogColors.RESET}"

handler = logging.StreamHandler()
handler.setFormatter(ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))
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

    def añadir(self, tupla: Tuple[str, ...]):
        if len(tupla) != self.n:
            raise ValueError(f"Todas las tuplas deben tener {self.n} individuos")
        self.tuplas.add(tupla)
        logger.debug(f"[{self.nombre}] Añadida tupla {tupla}")

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

    def asignar_individuo_a_categoria(self, id_: str, categoria: str, atributos: Dict[str, Union[str, int, bool]]):
        if categoria not in self.categorias:
            raise ValueError(f"La categoría '{categoria}' no existe")
        cat = self.categorias[categoria]
        for clave, valor in atributos.items():
            if clave not in cat.esquema or not isinstance(valor, cat.esquema[clave]):
                raise ValueError(f"Atributo {clave} inválido para la categoría {categoria}")
        self.individuos.registrar(id_, atributos)
        self.proposiciones[categoria].añadir((id_,))

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
        tupla = tuple(contexto[v] for v in self.variables)
        resultado = base.proposiciones[self.nombre_proposicion].existe(tupla)
        logger.debug(f"[{self.nombre_proposicion}] Validación simple {tupla} -> {resultado}")
        return resultado

class CondicionComparacion(Condicion):
    def __init__(self, lado_izq, comparador: TipoComparacion, lado_der, variables: List[str]):
        super().__init__(variables)
        self.lado_izq = lado_izq
        self.lado_der = lado_der
        self.comparador = comparador

    def _resolver_valor(self, expr, contexto, base: BaseConocimiento):
        if isinstance(expr, tuple) and len(expr) == 2:
            var, attr = expr
            id_ = contexto.get(var)
            return base.individuos.obtener(id_).get(attr)
        elif isinstance(expr, str) and expr in contexto:
            return contexto[expr]
        return expr

    def validar(self, contexto: Dict[str, str], base: BaseConocimiento) -> bool:
        val_izq = self._resolver_valor(self.lado_izq, contexto, base)
        val_der = self._resolver_valor(self.lado_der, contexto, base)
        resultado = OPERADORES[self.comparador](val_izq, val_der)
        logger.debug(f"[Comparacion] {val_izq} {self.comparador.value} {val_der} -> {resultado}")
        return resultado

class Consecuencia(ABC):
    def __init__(self, variables: List[str]):
        self.variables = variables

    @abstractmethod
    def ejecutar(self, contexto: Dict[str, str], base: BaseConocimiento):
        pass

class ConsecuenciaAsignacion(Consecuencia):
    def __init__(self, proposicion: str, parametros: List[Union[str, str]], variables: List[str]):
        super().__init__(variables)
        self.proposicion = proposicion
        self.parametros = parametros

    def ejecutar(self, contexto: Dict[str, str], base: BaseConocimiento):
        tupla = tuple(contexto.get(p, p) for p in self.parametros)
        if self.proposicion not in base.proposiciones:
            base.crear_proposicion(self.proposicion, len(tupla))
        logger.info(f"[Accion] Añadir {tupla} a {self.proposicion}")
        base.proposiciones[self.proposicion].añadir(tupla)

class ConsecuenciaEliminacion(Consecuencia):
    def __init__(self, proposicion: str, parametros: List[Union[str, str]], variables: List[str]):
        super().__init__(variables)
        self.proposicion = proposicion
        self.parametros = parametros

    def ejecutar(self, contexto: Dict[str, str], base: BaseConocimiento):
        tupla = tuple(contexto.get(p, p) for p in self.parametros)
        logger.info(f"[Accion] Eliminar {tupla} de {self.proposicion}")
        base.proposiciones[self.proposicion].eliminar(tupla)

class ConsecuenciaModificacion(Consecuencia):
    def __init__(self, objetivo: str, atributo: str, operacion: TipoOperacion,
                 valor: Union[str, int, Tuple[str, str]], atributo_valor: str = None, variables: List[str] = []):
        super().__init__(variables)
        self.objetivo = objetivo
        self.atributo = atributo
        self.operacion = operacion
        self.valor = valor
        self.atributo_valor = atributo_valor

    def ejecutar(self, contexto: Dict[str, str], base: BaseConocimiento):
        id_ = contexto.get(self.objetivo, self.objetivo)
        indiv = base.individuos.obtener(id_)
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

class Regla:
    def __init__(self, nombre: str, parametros: List[str], condiciones: List[Condicion]):
        self.nombre = nombre
        self.parametros = parametros
        self.condiciones = condiciones
        self.consecuencias: List[Consecuencia] = []

    def validar(self, valores: List[str], base: BaseConocimiento) -> bool:
        contexto = dict(zip(self.parametros, valores))
        logger.info(f"[Regla:{self.nombre}] Iniciar validación con contexto {contexto}")
        for cond in self.condiciones:
            ok = cond.validar(contexto, base)
            logger.debug(f"[Regla:{self.nombre}] Resultado condición '{type(cond).__name__}': {ok}")
            if not ok:
                logger.warning(f"[Regla:{self.nombre}] FALLA en contexto {contexto}")
                return False
        logger.info(f"[Regla:{self.nombre}] VALIDADA correctamente para {contexto}")
        return True

    def ejecutar(self, valores: List[str], base: BaseConocimiento):
        if self.validar(valores, base):
            logger.info(f"[Regla:{self.nombre}] Ejecutando consecuencia en {valores}")
            contexto = dict(zip(self.parametros, valores))
            for c in self.consecuencias:
                c.ejecutar(contexto, base)
            logger.info(f"[Regla:{self.nombre}] Consecuencias ejecutadas")

class MotorReglas:
    def __init__(self, base: BaseConocimiento):
        self.base = base
        self.reglas: List[Regla] = []
        self.acciones: List[Regla] = []

    def añadir_regla(self, regla: Regla, accion: bool = False):
        if accion:
            self.acciones.append(regla)
        else:
            self.reglas.append(regla)

    def ejecutar_accion(self, nombre_accion: str, valores: List[str]):
        for regla in self.acciones:
            if regla.nombre == nombre_accion:
                regla.ejecutar(valores, self.base)
                break


# (Aquí siguen las clases BaseConocimiento, Condicion, Regla, Consecuencia, MotorReglas, etc.)

if __name__ == "__main__":
    base = BaseConocimiento()
    base.crear_categoria("Usuario", {"nombre": str, "libros_prestados": int})
    base.crear_categoria("Libro", {"titulo": str})

    base.crear_proposicion("Prestamo", 2)
    base.crear_proposicion("LibroPrestado", 1)
    base.crear_proposicion("Disponible", 1)

    base.asignar_individuo_a_categoria("u1", "Usuario", {"nombre": "Juan", "libros_prestados": 0})
    base.asignar_individuo_a_categoria("u2", "Usuario", {"nombre": "Ana", "libros_prestados": 0})
    base.asignar_individuo_a_categoria("l1", "Libro", {"titulo": "El Quijote"})
    base.asignar_individuo_a_categoria("l2", "Libro", {"titulo": "1984"})
    base.asignar_individuo_a_categoria("l3", "Libro", {"titulo": "Fundación"})
    base.asignar_individuo_a_categoria("l4", "Libro", {"titulo": "Dune"})

    base.proposiciones["Disponible"].añadir(("l1",))
    base.proposiciones["Disponible"].añadir(("l2",))
    base.proposiciones["Disponible"].añadir(("l3",))
    base.proposiciones["Disponible"].añadir(("l4",))

    motor = MotorReglas(base)

    r1 = Regla("prestar_libro", ["u", "l"], [
        CondicionSimple("Usuario", ["u"]),
        CondicionSimple("Libro", ["l"]),
        CondicionSimple("Disponible", ["l"]),
        CondicionComparacion(("u", "libros_prestados"), TipoComparacion.MENOR, 3, ["u"])
    ])
    r1.consecuencias.append(ConsecuenciaAsignacion("Prestamo", ["u", "l"], ["u", "l"]))
    r1.consecuencias.append(ConsecuenciaModificacion("u", "libros_prestados", TipoOperacion.INCREMENTO, 1, variables=["u"]))
    r1.consecuencias.append(ConsecuenciaAsignacion("LibroPrestado", ["l"], ["l"]))
    r1.consecuencias.append(ConsecuenciaEliminacion("Disponible", ["l"], ["l"]))
    motor.añadir_regla(r1, accion=True)

    r2 = Regla("devolver_libro", ["u", "l"], [
        CondicionSimple("Prestamo", ["u", "l"])
    ])
    r2.consecuencias.append(ConsecuenciaEliminacion("Prestamo", ["u", "l"], ["u", "l"]))
    r2.consecuencias.append(ConsecuenciaModificacion("u", "libros_prestados", TipoOperacion.DECREMENTO, 1, variables=["u"]))
    r2.consecuencias.append(ConsecuenciaEliminacion("LibroPrestado", ["l"], ["l"]))
    r2.consecuencias.append(ConsecuenciaAsignacion("Disponible", ["l"], ["l"]))
    motor.añadir_regla(r2, accion=True)

    motor.ejecutar_accion("prestar_libro", ["u1", "l1"])
    motor.ejecutar_accion("prestar_libro", ["u1", "l2"])
    motor.ejecutar_accion("prestar_libro", ["u1", "l3"])
    motor.ejecutar_accion("prestar_libro", ["u1", "l4"])  # debe fallar, ya tiene 3 libros
    motor.ejecutar_accion("devolver_libro", ["u1", "l1"])
    motor.ejecutar_accion("prestar_libro", ["u1", "l4"])  # ahora sí debe funcionar
    motor.ejecutar_accion("prestar_libro", ["u2", "l2"])  # debe fallar, l2 está prestado
    motor.ejecutar_accion("devolver_libro", ["u1", "l2"])
    motor.ejecutar_accion("prestar_libro", ["u2", "l2"])  # ahora sí debe funcionar

    print("Préstamos:", base.proposiciones["Prestamo"].tuplas)
    print("LibroPrestado:", base.proposiciones["LibroPrestado"].tuplas)
    print("Disponible:", base.proposiciones["Disponible"].tuplas)
    print("Usuarios:", base.individuos.individuos)
