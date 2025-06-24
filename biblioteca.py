@User
def getUsuario(id):
    return "usuario_" + str(id)

def newUsuario(id, nombre):
    return {"id": id, "nombre": nombre}

def setusuario(id):
    pass


class User(object):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"User(id={self.id}, nombre={self.nombre})"

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre