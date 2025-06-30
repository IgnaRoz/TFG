from registry import Registry, export


class Biblioteca(Registry):

    @export
    def concederPrestamo(usuario,libro):
        print(f"[Biblioteca] Prestadmo del libro {libro} concedido al usuario {usuario}")
        return True
    @export
    def getUsuario():
        return "nacho"
    @export
    def print(mensaje):
        print(mensaje)
        return mensaje
