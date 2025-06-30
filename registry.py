# registry.py
from __future__ import annotations

def export(func):
    """Marca la función para el registro."""
    func._export = True
    return func

class Registry:
    """Base: construye cls.funcs con los métodos marcados."""
    funcs: dict[str, callable]

    def __init_subclass__(cls, **kw):
        super().__init_subclass__(**kw)
        cls.funcs = {}
        for name, obj in cls.__dict__.items():
            # desempaqueta staticmethod/classmethod si los usas
            if isinstance(obj, (staticmethod, classmethod)):
                func = obj.__func__
            else:
                func = obj

            if callable(func) and getattr(func, "_export", False):
                cls.funcs[name] = func
