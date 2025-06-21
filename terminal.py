#!/usr/bin/env python3
import sys
import shlex

class Terminal:

    def __init__(self, motor):

        self.motor = motor

    def procesar_linea(self, linea_raw):

        linea = linea_raw

        # 2) Tokenizar respetando comillas
        try:
            tokens = shlex.split(linea)
        except ValueError as e:
            print(f"Error de sintaxis: {e}")
            return

        if not tokens:
            return

        # 3) Comando principal
        verb = tokens[0].lower()
        if verb in ('exit', 'quit'):
            sys.exit(0)
        if verb not in ('run', 'new', 'add', 'load'):
            print("Error: comando no reconocido. Usa 'run', 'new', 'add' o 'load'.")
            return

        # 4) Manejar 'load' (sin parámetros entre comillas)
        if verb == 'load':
            if len(tokens) != 2:
                print("Uso: load <archivo>")
                return
            archivo = tokens[1]
            self.motor.set_archivo(archivo)
            self.motor.cargar_archivo()
            return

        # 5) Para run/new/add se esperan al menos un 'prop' y posibles parámetros
        
        elif verb  in ('run', 'new', 'add'):
            if len(tokens) < 2:
                print(f"Uso: {verb} <Comando> [param1] [param2] ...")
                return
            prop = tokens[1]
            params = []
            # Intentar convertir parámetros numéricos a int
            for p in tokens[2:]:
                if p.isdigit():
                    params.append(int(p))
                else:
                    params.append(p)

            # 6) Despachar subcomando
            if verb == 'run':
                self.ejecutar_comando_run(prop, params)
            elif verb == 'new':
                self.ejecutar_comando_new(prop, params)
            elif verb == 'add':
                self.ejecutar_comando_add(prop, params)
        else:
            print(f"Error: comando '{verb}' no reconocido. Usa 'run', 'new', 'add' o 'load'.")

    def ejecutar_comando_run(self, prop, params):
        self.motor.ejecutar_accion(prop, params)

    def ejecutar_comando_new(self, prop, params):
        self.motor.nuevo_individuo(prop, params)

    def ejecutar_comando_add(self, prop, params):
        self.motor.add_proposicion(prop, params)

    def run(self):
        """
        Inicia el bucle interactivo de la terminal.
        """
        while True:
            try:
                linea = input('> ')
            except EOFError:
                break
            self.procesar_linea(linea)


def main():
    # Ejemplo de uso con motor simulado
    class MotorDummy:
        def set_archivo(self, f): print(f"[Motor] Archivo seteado: {f}")
        def cargar_archivo(self): print("[Motor] Archivo cargado.")
        def ejecutar_accion(self, c, p): print(f"[Motor] Ejecutar {c} con {p}")
        def nuevo_individuo(self, c, p): print(f"[Motor] Nuevo individuo {c} con {p}")
        def add_proposicion(self, c, p): print(f"[Motor] Añadir proposición {c} con {p}")

    term = Terminal(MotorDummy())
    term.run()

if __name__ == '__main__':
    main()
