from typing import List

from base import (
    BaseConocimiento,
    TipoComparacion,
    TipoOperacion,
    logger,
)
from condiciones import CondicionSimple, CondicionComparacion
from consecuencias import (
    ConsecuenciaAsignacion,
    ConsecuenciaEliminacion,
    ConsecuenciaModificacion,
)
from reglas import Regla


class MotorEjecucion:
    def __init__(self, base: BaseConocimiento):
        self.base = base
        self.reglas: List[Regla] = []
        self.acciones: List[Regla] = []
        self.archivo = None

    def add_regla(self, regla: Regla, accion: bool = False):
        if accion:
            self.acciones.append(regla)
        else:
            self.reglas.append(regla)

    def ejecutar_accion(self, nombre_accion: str, valores: List[str]):
        for regla in self.acciones:
            if regla.nombre == nombre_accion:
                regla.ejecutar(valores, self.base)
                break

    # Nuevas utilidades -------------------------------------------------
    def set_archivo(self, ruta: str):
        self.archivo = ruta

    def cargar_archivo(self):
        if not self.archivo:
            return
        from antlr4 import FileStream, CommonTokenStream
        from gramaticaLexer import gramaticaLexer
        from gramaticaParser import gramaticaParser
        from motor_visitor import MotorVisitor

        stream = FileStream(self.archivo, encoding="utf-8")
        lexer = gramaticaLexer(stream)
        tokens = CommonTokenStream(lexer)
        parser = gramaticaParser(tokens)
        tree = parser.programa()
        visitor = MotorVisitor(self)
        visitor.visit(tree)

    # Métodos para el visitor ------------------------------------------
    def crear_categoria(self, nombre: str, esquema: dict):
        self.base.crear_categoria(nombre, esquema)

    def crear_proposicion(self, nombre: str, n: int):
        self.base.crear_proposicion(nombre, n)

    def nuevo_individuo(self, nombre: str, args: List):
        if nombre not in self.base.categorias:
            return
        esquema = list(self.base.categorias[nombre].esquema.keys())
        atributos = dict(zip(esquema, args[1:])) if esquema else {}
        id_ = args[0] if args else nombre
        self.base.asignar_individuo_a_categoria(id_, nombre, atributos)

    def add_proposicion(self, nombre: str, valores: List):
        if nombre in self.base.proposiciones:
            self.base.proposiciones[nombre].add(tuple(valores))


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

    base.proposiciones["Disponible"].add(("l1",))
    base.proposiciones["Disponible"].add(("l2",))
    base.proposiciones["Disponible"].add(("l3",))
    base.proposiciones["Disponible"].add(("l4",))

    motor = MotorEjecucion(base)

    r1 = Regla(
        "prestar_libro",
        ["u", "l"],
        [
            CondicionSimple("Usuario", ["u"]),
            CondicionSimple("Libro", ["l"]),
            CondicionSimple("Disponible", ["l"]),
            CondicionComparacion(("u", "libros_prestados"), TipoComparacion.MENOR, 3, ["u"]),
        ],
    )
    r1.consecuencias.append(ConsecuenciaAsignacion("Prestamo", ["u", "l"], ["u", "l"]))
    r1.consecuencias.append(
        ConsecuenciaModificacion("u", "libros_prestados", TipoOperacion.INCREMENTO, 1, variables=["u"])
    )
    r1.consecuencias.append(ConsecuenciaAsignacion("LibroPrestado", ["l"], ["l"]))
    r1.consecuencias.append(ConsecuenciaEliminacion("Disponible", ["l"], ["l"]))
    motor.add_regla(r1, accion=True)

    r2 = Regla(
        "devolver_libro",
        ["u", "l"],
        [CondicionSimple("Prestamo", ["u", "l"])],
    )
    r2.consecuencias.append(ConsecuenciaEliminacion("Prestamo", ["u", "l"], ["u", "l"]))
    r2.consecuencias.append(
        ConsecuenciaModificacion("u", "libros_prestados", TipoOperacion.DECREMENTO, 1, variables=["u"])
    )
    r2.consecuencias.append(ConsecuenciaEliminacion("LibroPrestado", ["l"], ["l"]))
    r2.consecuencias.append(ConsecuenciaAsignacion("Disponible", ["l"], ["l"]))
    motor.add_regla(r2, accion=True)

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
