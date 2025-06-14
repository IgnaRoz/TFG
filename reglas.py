from typing import List

from base import BaseConocimiento, logger
from condiciones import Condicion
from consecuencias import Consecuencia


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
