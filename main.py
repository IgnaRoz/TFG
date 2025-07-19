import argparse
import logging
from base import BaseConocimiento, TipoComparacion, TipoOperacion
from condiciones import CondicionSimple, CondicionComparacion
from consecuencias import (
    ConsecuenciaAsignacion,
    ConsecuenciaEliminacion,
    ConsecuenciaModificacion,
)
from reglas import Regla
from motorEjecucion import MotorEjecucion


def parse_args() -> argparse.Namespace:
    """Parses command line options for the main entry point."""
    parser = argparse.ArgumentParser(
        description="Motor de reglas interactivo"
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Nivel de logging",
    )
    # Argumentos reservados para futuras ampliaciones
    #parser.add_argument(
    #    "--archivo",
    #    help="Archivo de reglas a cargar al iniciar",
    #)
    #parser.add_argument(
    #    "--import-dir",
    #    help="Directorio de importaciones",
    #)
    return parser.parse_args()

if __name__ == "__main__":
    
    args = parse_args()
    # Configura el nivel de logging elegido
    logging.getLogger("LOG").setLevel(getattr(logging, args.log_level))
    base = BaseConocimiento()


    motor = MotorEjecucion(base)

    #motor.set_archivo("ejemplo.txt")
   # motor.cargar_archivo()

    motor.run_terminal()