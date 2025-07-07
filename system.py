from registry import Registry, export


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
    def count():
        pass
    def max():
        pass
    def min():
        pass