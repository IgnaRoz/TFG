from typing import Tuple
from base import Proposicion

class Output(Proposicion):
    def __init__(self):
        super().__init__("Output", [])


    def add(self, entrada):
        # Verifica que la entrada sea una tupla con al menos un elemento
        if not isinstance(entrada, tuple) or len(entrada) < 1:
            raise ValueError("La entrada debe ser una tupla con al menos un elemento")
        if not isinstance(entrada[0], str):
            raise ValueError("La entrada debe ser una cadena de texto")
        print(f"Output: {self.procesarString(entrada)}")
        return True
    def eliminar(self, entrada: str):
        # Hace lo mismo que add
        # Verifica que la entrada sea una tupla con al menos un elemento
        if not isinstance(entrada, tuple) or len(entrada) < 1:
            raise ValueError("La entrada debe ser una tupla con al menos un elemento")
        if not isinstance(entrada[0], str):
            raise ValueError("La entrada debe ser una cadena de texto")
        print(f"Output: {self.procesarString(entrada)}")
        return True

    def existe(self, entrada: str) -> bool:

        # Verifica que la entrada sea una tupla con al menos un elemento
        if not isinstance(entrada, tuple) or len(entrada) < 1:
            raise ValueError("La entrada debe ser una tupla con al menos un elemento")
        if not isinstance(entrada[0], str):
            raise ValueError("La entrada debe ser una cadena de texto")
        print(f"Output: {self.procesarString(entrada)}")
        return True
    
    def procesarString(self, entrada):
        #Sustituye los valores {n} por los valores de entrada
        plantilla = entrada[0]
        salida = plantilla.format(*entrada[1:])
        
        
        
        return salida