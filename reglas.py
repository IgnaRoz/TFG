from typing import List

import logging
from base import BaseConocimiento
logger = logging.getLogger("LOG")
from condiciones import Condicion
from consecuencias import Consecuencia


class Regla:
    def __init__(self, nombre: str, parametros: List[str], condiciones: List[Condicion], descripcion: str = None):
        self.nombre = nombre
        self.parametros = parametros
        self.condiciones = condiciones
        self.consecuencias: List[Consecuencia] = []
        self.descripcion = descripcion if descripcion else f"Proposición {nombre}: Sin descripción"

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
