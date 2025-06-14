from base import BaseConocimiento, TipoComparacion, TipoOperacion
from condiciones import CondicionSimple, CondicionComparacion
from consecuencias import (
    ConsecuenciaAsignacion,
    ConsecuenciaEliminacion,
    ConsecuenciaModificacion,
)
from reglas import Regla
from motorEjecucion import MotorEjecucion


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
