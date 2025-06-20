from abc import ABC, abstractmethod
from typing import Dict, List, Tuple, Union

import logging
from base import BaseConocimiento, TipoOperacion

logger = logging.getLogger(__name__)


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
        logger.info(f"[Accion] Add {tupla} to {self.proposicion}")
        base.proposiciones[self.proposicion].add(tupla)


class ConsecuenciaEliminacion(Consecuencia):
    def __init__(self, proposicion: str, parametros: List[Union[str, str]], variables: List[str]):
        super().__init__(variables)
        self.proposicion = proposicion
        self.parametros = parametros

    def ejecutar(self, contexto: Dict[str, str], base: BaseConocimiento):
        tupla = tuple(contexto.get(p, p) for p in self.parametros)
        if self.proposicion not in base.proposiciones:
            raise ValueError(f"Proposición '{self.proposicion}' no existe")
        logger.info(f"[Accion] Eliminar {tupla} de {self.proposicion}")
        base.proposiciones[self.proposicion].eliminar(tupla)


class ConsecuenciaModificacion(Consecuencia):
    def __init__(
        self,
        objetivo: str,
        atributo: str,
        operacion: TipoOperacion,
        valor: Union[str, int, Tuple[str, str]],
        atributo_valor: str = None,
        variables: List[str] = None,
    ):
        super().__init__(variables or [])
        self.objetivo = objetivo
        self.atributo = atributo
        self.operacion = operacion
        self.valor = valor
        self.atributo_valor = atributo_valor

    def ejecutar(self, contexto: Dict[str, str], base: BaseConocimiento):
        id_ = contexto.get(self.objetivo, self.objetivo)
        indiv = base.individuos.obtener(id_)
        if indiv is None:
            raise ValueError(f"Individuo '{id_}' no existe")
        if self.atributo not in indiv:
            raise ValueError(f"Atributo '{self.atributo}' no existe en '{id_}'")
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
