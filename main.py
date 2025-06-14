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


    motor = MotorEjecucion(base)

    motor.set_archivo("ejemplo.txt")
    motor.cargar_archivo()