# func_store.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Any, Dict, Tuple

@dataclass
class _Entry:
    """Contiene la función + sus parámetros por defecto."""
    func: Callable[..., Any]
    args: Tuple[Any, ...] = field(default_factory=tuple)
    kwargs: Dict[str, Any] = field(default_factory=dict)

    def run(self, *override_args, **override_kwargs) -> Any:
        """
        Ejecuta la función.
        • Si se pasan argumentos, reemplazan a los guardados.
        • Los kwargs nuevos se mezclan con los guardados (ganan los nuevos).
        """
        final_args   = override_args or self.args
        final_kwargs = {**self.kwargs, **override_kwargs}
        return self.func(*final_args, **final_kwargs)


class FuncStore:
    """
    Almacén ligero de callables parametrizados.
    Ejemplo de uso:
        store = FuncStore()
        store.register("saludo", print, "Hola")
        store.execute("saludo")                  # Hola
    """
    def __init__(self) -> None:
        self._registry: dict[str, _Entry] = {}

    # ─────────────────────────────────────────────
    # Registro
    # ─────────────────────────────────────────────
    def register(self, name: str,
                 func: Callable[..., Any],
                 *args: Any, **kwargs: Any) -> None:
        """Guarda la función y argumentos."""
        if name in self._registry:
            raise KeyError(f"Ya existe una entrada llamada '{name}'")
        self._registry[name] = _Entry(func, args, kwargs)

    def unregister(self, name: str) -> None:
        """Elimina la entrada."""
        self._registry.pop(name)

    # ─────────────────────────────────────────────
    # Ejecución
    # ─────────────────────────────────────────────
    def execute(self, name: str,
                *args: Any, **kwargs: Any) -> Any:
        """
        Lanza la función almacenada.
        Si pasas args/kwargs aquí, sustituyen a los guardados.
        """
        try:
            entry = self._registry[name]
        except KeyError:
            raise KeyError(f"No hay ninguna entrada '{name}' registrada")

        return entry.run(*args, **kwargs)

    # ─────────────────────────────────────────────
    # Accesos de conveniencia
    # ─────────────────────────────────────────────
    def __contains__(self, name: str) -> bool:
        return name in self._registry

    def __getitem__(self, name: str) -> _Entry:
        return self._registry[name]

    def list(self) -> tuple[str, ...]:
        """Devuelve los nombres registrados (solo lectura)."""
        return tuple(self._registry)


# ─────────────────────────────────────────────
# DEMO RÁPIDA
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # 1) funciones de ejemplo
    def sumar(a, b): return a + b
    def eco(msg, veces=1): print(msg * veces)

    # 2) crear almacén y registrar
    store = FuncStore()
    store.register("suma10", sumar, 10, 5)      # 10 + 5
    store.register("hola3", eco, "hola ", 3)

    # 3) ejecutar tal cual
    print(store.execute("suma10"))              # → 15
    store.execute("hola3")                      # hola hola hola 

    # 4) sobrescribir argumentos al vuelo
    print(store.execute("suma10", 42, 8))       # → 50
