from registry import Registry, export


class Biblioteca(Registry):

    @export
    def concederPrestamo(usuario,libro):
        print(f"[Biblioteca] Prestamo del libro {libro} concedido al usuario {usuario}")
        return True
    @export
    def getUsuario():
        return "nacho"
    
    @export
    def Count(variable):
        if isinstance(variable,list):
            print(f"Variable {variable} count:{len(variable)} ")
            return len(variable)
        return 1
    @export
    def print(mensaje):
        print(mensaje)
        return mensaje
