from abc import ABC, abstractmethod
from typing import Dict, List

import logging
from base import BaseConocimiento, OPERADORES, TipoComparacion

logger = logging.getLogger("LOG")


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
        if self.nombre_proposicion not in base.proposiciones:
            raise ValueError(f"Proposición '{self.nombre_proposicion}' no existe")
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
            indiv = base.individuos.obtener(id_)
            if indiv is None:
                raise ValueError(f"Individuo '{id_}' no existe")
            return indiv.get(attr)
        elif isinstance(expr, str) and expr in contexto:
            return contexto[expr]
        return expr

    def validar(self, contexto: Dict[str, str], base: BaseConocimiento) -> bool:
        val_izq = self._resolver_valor(self.lado_izq, contexto, base)
        val_der = self._resolver_valor(self.lado_der, contexto, base)
        resultado = OPERADORES[self.comparador](val_izq, val_der)
        logger.debug(f"[Comparacion] {val_izq} {self.comparador.value} {val_der} -> {resultado}")
        return resultado
