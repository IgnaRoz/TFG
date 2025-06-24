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
        parametros = []
        #Si es una variable, se sustituye por su valor en el contexto
        #Si no, se deja como está, puede ser un valor literal o individuo
        for v in self.variables:
            if v not in contexto:
                parametros.append(v)
            else: 
                parametros.append(contexto[v])
        tupla = tuple(parametros)
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


class CondicionLogica(Condicion):
    def __init__(self, condiciones: List[Condicion], operador: str):
        super().__init__([])
        self.condiciones = condiciones
        self.operador = operador

    def validar(self, contexto: Dict[str, str], base: BaseConocimiento) -> bool:
        if self.operador == "AND":
            logger.debug(f"[CondicionLogica] Validando condiciones con AND")
            resultado = all(condicion.validar(contexto, base) for condicion in self.condiciones)
        elif self.operador == "OR":
            logger.debug(f"[CondicionLogica] Validando condiciones con OR")
            resultado = any(condicion.validar(contexto, base) for condicion in self.condiciones)
        else:
            raise ValueError(f"Operador lógico '{self.operador}' no reconocido")
        logger.debug(f"[CondicionLogica] Resultado {self.operador} -> {resultado}")
        return resultado
    
class CondicionNegacion(Condicion):
    def __init__(self, condicion: Condicion):
        super().__init__(condicion.variables)
        self.condicion = condicion

    def validar(self, contexto: Dict[str, str], base: BaseConocimiento) -> bool:
        logger.debug(f"[CondicionNegacion] Validando condición de negación")
        resultado = not self.condicion.validar(contexto, base)
        logger.debug(f"[CondicionNegacion] Resultado NOT -> {resultado}")
        return resultado