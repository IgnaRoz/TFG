from registry import Registry, export
from base import ElementoProposicion
import builtins

class System(Registry):

    @export
    def print(template: str, *args, **kwargs):
        try:
            mensaje = template.format(*args, **kwargs)
        except (IndexError, KeyError) as e:
            raise ValueError(
            f"Faltan argumentos al rellenar la plantilla:\n{e}"
        ) from None
        print(mensaje)
        return True

    @export
    def count(lista):
        """Devuelve la cantidad de elementos de *lista*.

        Se asegura de que el parámetro recibido sea una lista.
        """
        if isinstance(lista, list):
            
            return len(lista)
        return 1

    @export
    def max(lista, atributo=None):
        """Devuelve el elemento máximo de la lista.

        Si se indica *atributo* y los elementos son ``ElementoProposicion``,
        se selecciona el elemento cuyo atributo tenga el mayor valor.
        En otro caso, los elementos deben ser enteros.
        """
        if not isinstance(lista, list):
            raise ValueError("System.max espera una lista")
        if not lista:
            raise ValueError("La lista está vacía")

        if atributo is not None:
            for elem in lista:
                if not isinstance(elem, ElementoProposicion):
                    raise ValueError(
                        "System.max con atributo requiere elementos ElementoProposicion"
                    )
                if atributo not in elem.atributos:
                    raise ValueError(
                        f"El elemento {elem} no tiene el atributo '{atributo}'"
                    )
            return builtins.max(lista, key=lambda e: e.atributos[atributo])

        for elem in lista:
            if not isinstance(elem, int):
                raise ValueError("System.max espera enteros si no se usa atributo")
        return builtins.max(lista)

    @export
    def min(lista, atributo=None):
        """Devuelve el elemento mínimo de la lista.

        Si se indica *atributo* y los elementos son ``ElementoProposicion``,
        se selecciona el elemento cuyo atributo tenga el valor mínimo.
        En otro caso, los elementos deben ser enteros.
        """
        if not isinstance(lista, list):
            raise ValueError("System.min espera una lista")
        if not lista:
            raise ValueError("La lista está vacía")

        if atributo is not None:
            for elem in lista:
                if not isinstance(elem, ElementoProposicion):
                    raise ValueError(
                        "System.min con atributo requiere elementos ElementoProposicion"
                    )
                if atributo not in elem.atributos:
                    raise ValueError(
                        f"El elemento {elem} no tiene el atributo '{atributo}'"
                    )
            return builtins.min(lista, key=lambda e: e.atributos[atributo])

        for elem in lista:
            if not isinstance(elem, int):
                raise ValueError("System.min espera enteros si no se usa atributo")
        return builtins.min(lista)
    
    @export
    def sum(lista, atributo=None):
        """Suma los valores de una lista.

        Si se indica *atributo* y los elementos son ``ElementoProposicion``,
        suma el valor de ese atributo en cada elemento.
        En otro caso, suma los valores enteros de la lista.
        """
        if not isinstance(lista, list):
            raise ValueError("System.sum espera una lista")
        # Si la lista está vacía, devolvemos 0
        if not lista:
            return 0

        if atributo is not None:
            total = 0
            for elem in lista:
                if not isinstance(elem, ElementoProposicion):
                    raise ValueError(
                        "System.sum con atributo requiere elementos ElementoProposicion"
                    )
                if atributo not in elem.atributos:
                    raise ValueError(
                        f"El elemento {elem} no tiene el atributo '{atributo}'"
                    )
                total += elem.atributos[atributo]
            return total

        total = 0
        for elem in lista:
            if not isinstance(elem, int):
                raise ValueError("System.sum espera enteros si no se usa atributo")
            total += elem
        return total