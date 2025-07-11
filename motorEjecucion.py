from typing import List
from datetime import date, timedelta
from terminal import Terminal
import logging
from base import (
    BaseConocimiento,
    TipoComparacion,
    TipoOperacion,
)
from condiciones import CondicionSimple, CondicionComparacion, CondicionAsignacion, CondicionFuncion
from consecuencias import (
    ConsecuenciaAsignacion,
    ConsecuenciaEliminacion,
    ConsecuenciaModificacion,
    ConsecuenciaFuncion,
)
from reglas import Regla, Contingencia
from func import func
#from system import Output

class LogColors:
    DEBUG = "\033[94m"
    INFO = "\033[92m"
    WARNING = "\033[93m"
    ERROR = "\033[91m"
    RESET = "\033[0m"


class ColoredFormatter(logging.Formatter):
    LEVEL_COLOR = {
        "DEBUG": LogColors.DEBUG,
        "INFO": LogColors.INFO,
        "WARNING": LogColors.WARNING,
        "ERROR": LogColors.ERROR,
        "CRITICAL": LogColors.ERROR,
    }

    def format(self, record):
        color = self.LEVEL_COLOR.get(record.levelname, LogColors.RESET)
        message = super().format(record)
        return f"{color}{message}{LogColors.RESET}"


handler = logging.StreamHandler()
handler.setFormatter(
    ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
)
logger = logging.getLogger("LOG")
logger.setLevel(logging.DEBUG)
logger.handlers = [handler]


from antlr4.error.ErrorListener import ErrorListener as AntlrErrorListener


class ErrorListener(AntlrErrorListener):
    def __init__(self):
        self.errores = []  
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        token = getattr(offendingSymbol, "text", str(offendingSymbol))
        #logger.error(f"Error {line}:{column} en '{token}': {msg}")
        self.errores.append(f"Error {line}:{column} en '{token}': {msg}")
    

        


class MotorEjecucion:
    def __init__(self, base: BaseConocimiento):
        self.base = base
        self.reglas: List[Regla] = []
        self.acciones: List[Regla] = []
        self.archivo = None
        #Incializar el motor
        #self.base.proposiciones["Output"] = Output()

    def get_regla(self, nombre: str) -> Regla:
        for regla in self.reglas:
            if regla.nombre == nombre:
                return regla
        return None
    def get_accion(self, nombre: str) -> Regla:
        for accion in self.acciones:
            if accion.nombre == nombre:
                return accion
        return None
    def get_acciones(self) -> List[Regla]:
        return self.acciones
    def get_proposicion(self, nombre: str) -> str:
        if nombre in self.base.proposiciones:
            return self.base.proposiciones[nombre]
        return None
    def get_proposiciones(self) -> List[str]:
        return list(self.base.proposiciones.values())
    def add_regla(self, regla: Regla, accion: bool = False):
        if accion:
            self.acciones.append(regla)
        else:
            self.reglas.append(regla)
    #Modificar, deberia poder obtener directamente la regla por su nombre(opcional)
    def ejecutar_accion(self, nombre_accion: str, valores: List[str]):
        aux = False
        for regla in self.acciones:
            if regla.nombre == nombre_accion:
                regla.ejecutar(valores, self.base)
                aux = True
                break
        if not aux:
            raise ValueError(f"No se ha econtrado la accion: {nombre_accion}")

    # Nuevas utilidades -------------------------------------------------
    def set_archivo(self, ruta: str):
        self.archivo = ruta

    def reset(self):
        """Elimina todas las reglas y proposiciones cargadas."""
        self.reglas.clear()
        self.acciones.clear()
        self.base = BaseConocimiento()

    def cargar_archivo(self):
        if not self.archivo:
            return
        from antlr4 import FileStream, CommonTokenStream
        from gramaticaLexer import gramaticaLexer
        from gramaticaParser import gramaticaParser
        from motor_visitor import MotorVisitor
        try:

            stream = FileStream(self.archivo, encoding="utf-8")
        except FileNotFoundError:
            logger.error(f"Archivo no encontrado: {self.archivo}")
            return
        lexer = gramaticaLexer(stream)
        parser_error = ErrorListener()
        lexer.removeErrorListeners()
        lexer.addErrorListener(parser_error)
        tokens = CommonTokenStream(lexer)
        parser = gramaticaParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(parser_error)
        tree = parser.programa()
        if parser_error.errores:
            for error in parser_error.errores:
                logger.error(error)
            return

        visitor = MotorVisitor(self)
        visitor.visit(tree)
    def run_terminal(self):    
        """
        Inicia la terminal interactiva para ejecutar comandos.
        """
        terminal = Terminal(self)
        terminal.run()    

    # Métodos para el visitor ------------------------------------------
    def crear_categoria(self, nombre: str, esquema: dict):
        self.base.crear_categoria(nombre, esquema)

    def crear_proposicion(self, nombre: str, parametros:List[str],descripcion: str = None, atributos = None,padre=None):
        if padre:
            if padre not in self.base.proposiciones:
                raise ValueError(f"No se ha econtrado la proposicion padre {padre} para la proposicion {nombre}")
            padre = self.base.proposiciones[padre]
        self.base.crear_proposicion(nombre, parametros,descripcion,atributos=atributos,padre=padre)

    def nuevo_individuo(self, nombre: str, args: List):
        if nombre not in self.base.categorias:
            return
        esquema = list(self.base.categorias[nombre].esquema.keys())
        atributos = dict(zip(esquema, args[1:])) if esquema else {}
        id_ = args[0] if args else nombre
        self.base.asignar_individuo_a_categoria(id_, nombre, atributos)

    def add_proposicion(self, nombre: str, valores: List,atributos=None):
        if nombre in self.base.proposiciones:
            elemento=self.base.proposiciones[nombre].add(tuple(valores),atributos=atributos)
            #añadir a individuos


if __name__ == "__main__":
    base = BaseConocimiento()
    #base.crear_categoria("Usuario", {"nombre": str, "libros_prestados": int})
    #base.crear_categoria("Libro", {"titulo": str})

    base.crear_proposicion("Prestamo", ["Usuario", "Libro"],atributos=["fecha_devolucion"])
    base.crear_proposicion("LibroPrestado", ["Libro"])
    base.crear_proposicion("Disponible", ["Libro"])
    base.crear_proposicion("Usuario", ["Usuario"])
    base.crear_proposicion("Libro", ["Libro"])
   # base.asignar_individuo_a_categoria("u1", "Usuario", {"nombre": "Juan", "libros_prestados": 0})
   # base.asignar_individuo_a_categoria("u2", "Usuario", {"nombre": "Ana", "libros_prestados": 0})
   # base.asignar_individuo_a_categoria("l1", "Libro", {"titulo": "El Quijote"})
   # base.asignar_individuo_a_categoria("l2", "Libro", {"titulo": "1984"})
   # base.asignar_individuo_a_categoria("l3", "Libro", {"titulo": "Fundación"})
   # base.asignar_individuo_a_categoria("l4", "Libro", {"titulo": "Dune"})

    base.proposiciones["Disponible"].add(("l1",))
    base.proposiciones["Disponible"].add(("l2",))
    base.proposiciones["Disponible"].add(("l3",))
    base.proposiciones["Disponible"].add(("l4",))

    base.proposiciones["Prestamo"].add(("u1", "l1"))
    base.proposiciones["Prestamo"].add(("u1", "l2"),atributos={"fecha_devolucion":date.today() + timedelta(days=15)})    
    base.proposiciones["Prestamo"].add(("u1", "l3"),atributos={"fecha_devolucion":date.today() + timedelta(days=15)})

    motor = MotorEjecucion(base)

    r1 = Regla(
        "prestar_libro",
        ["u"],
        [
            CondicionAsignacion(["u", "_"], "P","Prestamo"),
            CondicionSimple("Output", ["Condicion:Prestamo Usuario {0} con libro {1}","P.Usuario","P.Libro"])
        ],
    )
    r1.consecuencias.append(ConsecuenciaAsignacion("Output", ["Consecuencia:Prestamo Usuario {0} con libro {1} y fecha de devolucion {2}","P.Usuario","P.Libro","P.fecha_devolucion"]))
    motor.add_regla(r1, accion=True)

    motor.ejecutar_accion("prestar_libro", ["u1"])
    #motor.ejecutar_accion("prestar_libro", ["u1", "l2"])
    #motor.ejecutar_accion("prestar_libro", ["u1", "l3"])
    #motor.ejecutar_accion("prestar_libro", ["u1", "l4"])  # debe fallar, ya tiene 3 libros
    #motor.ejecutar_accion("devolver_libro", ["u1", "l1"])
    #motor.ejecutar_accion("prestar_libro", ["u1", "l4"])  # ahora sí debe funcionar
    #motor.ejecutar_accion("prestar_libro", ["u2", "l2"])  # debe fallar, l2 está prestado
    #motor.ejecutar_accion("devolver_libro", ["u1", "l2"])
    #motor.ejecutar_accion("prestar_libro", ["u2", "l2"])  # ahora sí debe funcionar
#
    #print("Préstamos:", base.proposiciones["Prestamo"].tuplas)
    #print("LibroPrestado:", base.proposiciones["LibroPrestado"].tuplas)
    #print("Disponible:", base.proposiciones["Disponible"].tuplas)
    #print("Usuarios:", base.individuos.individuos)
