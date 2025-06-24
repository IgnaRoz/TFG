from typing import Tuple
from base import Proposicion

class Output(Proposicion):
    def __init__(self):
        super().__init__("Output", 1)


    def add(self, entrada: Tuple[str, ...]):
        # Verifica que la entrada sea una tupla con al menos un elemento
        if not isinstance(entrada, tuple) or len(entrada) < 1:
            raise ValueError("La entrada debe ser una tupla con al menos un elemento")
        if not isinstance(entrada[0], str):
            raise ValueError("La entrada debe ser una cadena de texto")
        print(f"Output: {self.procesarString(entrada)}")
    def eliminar(self, entrada: str):
        # Hace lo mismo que add
        # Verifica que la entrada sea una tupla con al menos un elemento
        if not isinstance(entrada, tuple) or len(entrada) < 1:
            raise ValueError("La entrada debe ser una tupla con al menos un elemento")
        if not isinstance(entrada[0], str):
            raise ValueError("La entrada debe ser una cadena de texto")
        print(f"Output: {self.procesarString(entrada)}")

    def existe(self, entrada: str) -> bool:

        # Verifica que la entrada sea una tupla con al menos un elemento
        if not isinstance(entrada, tuple) or len(entrada) < 1:
            raise ValueError("La entrada debe ser una tupla con al menos un elemento")
        if not isinstance(entrada[0], str):
            raise ValueError("La entrada debe ser una cadena de texto")
        print(f"Output: {self.procesarString(entrada)}")
    
    def procesarString(self, entrada):
        #el primer elemento de la tupla es el mensaje a imprimir, el caracter % seguido de un numero( %2) indica que se debe sustiruir por el correspondiente elemento de la tupla(entrada[2])
        salida = entrada[0]
        for i in range(1, len(entrada)):
            salida = salida.replace(f"%{i}", str(entrada[i]))
        return salida