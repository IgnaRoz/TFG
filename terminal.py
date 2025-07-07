#!/usr/bin/env python3
import sys
import shlex

COMANDOS = {
    'run': {
        'uso': 'run <accion> [param1] [param2] ...',
        'descripcion': 'Ejecuta una acción con los parámetros dados.'
    },
    'add': {
        'uso': 'add <proposicion> [param1] [param2] ... <nombre_atributo1>:<valor1> ...',
        'descripcion': 'Añade una proposición con parámetros y atributos.'
    },
    'load': {
        'uso': 'load <archivo>',
        'descripcion': 'Carga un archivo de configuración.'
    },
    'reset': {
        'uso': 'reset',
        'descripcion': 'Elimina todas las reglas y proposiciones cargadas.'
    },
    'exit': {
        'uso': 'exit',
        'descripcion': 'Sale del programa.'
    },
    'quit': {
        'uso': 'quit',
        'descripcion': 'Sale del programa.'
    },
    'help': {
        'uso': 'help [comando] \nhelp accion <nombre accion> \nhelp proposicion <nombre proposicion>' ,
        'descripcion': 'Muestra ayuda general, de un comando específico o informacion sobre una accion o proposicion.'
    },
    'get': {
        'uso': 'get proposicion <nombre_proposicion>',
        'descripcion': 'Obtiene todos los elementos de una proposición específica.'
    },
    'acciones': {
        'uso': 'acciones',
        'descripcion': 'Lista todas las acciones disponibles.'
    },
    'proposiciones': {
        'uso': 'proposiciones',
        'descripcion': 'Lista todas las proposiciones disponibles.'
    },
}
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
        if verb not in COMANDOS:
            print(f"Error: comando no reconocido. Comandos disponibles: {', '.join(COMANDOS.keys())}")
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

        # 5) Para run/add se esperan al menos un 'prop' y posibles parámetros
        elif verb == 'reset':
            # Reinicia el motor borrando reglas y proposiciones
            self.motor.reset()
            print("Motor reiniciado")
            return
        elif verb == 'run':
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
            self.ejecutar_comando_run(prop, params)
        elif verb == 'add':
            if len(tokens) < 2:
                print(f"Uso: {verb} <Comando> [param1] [param2] ...")
                return
            prop = tokens[1]


            raw_args = tokens[2:]

            attr_index = None
            for idx, arg in enumerate(raw_args):
                if ':' in arg:
                    attr_index = idx
                    break

            params_raw = raw_args[:attr_index] if attr_index is not None else raw_args
            attrs_raw = raw_args[attr_index:] if attr_index is not None else []

            # Validar orden: atributos después de parámetros
            for a in attrs_raw:
                if ':' not in a:
                    print(f"Error al añadir proposición: parámetro '{a}' después de atributos no permitido")
                    return
            for p in params_raw:
                if ':' in p:
                    print(f"Error al añadir proposición: atributo '{p}' antes de parámetros no permitido")
                    return

            # Convertir parámetros
            params = [int(p) if p.isdigit() else p for p in params_raw]
            # Parsear atributos en diccionario
            attrs = {}
            for a in attrs_raw:
                key, val = a.split(':', 1)
                attrs[key] = int(val) if val.isdigit() else val

            try:
                self.ejecutar_comando_add(prop, params, attrs)
            except ValueError as e:
                print(f"Error al añadir proposición: {e}")
            return

                
        elif verb == 'help':

            if len(tokens) > 1:

                sub = tokens[1].lower()
                if sub == "accion":
                    nombre_accion = tokens[2] if len(tokens) > 2 else None
                    if nombre_accion:
                        accion = self.motor.get_accion(nombre_accion)
                        if accion:
                            print(f"Detalles de la acción '{nombre_accion}':")
                            print(accion.descripcion)
                        else:
                            print(f"No se encontró la acción '{nombre_accion}'.")
                    else:
                        info = COMANDOS['help']
                        print(f"Uso:\n{info['uso']}")
                        print(f"Descripcion: \n{info['descripcion']}")
                
                elif sub == "proposicion":
                    nombre_proposicion = tokens[2] if len(tokens) > 2 else None
                    if nombre_proposicion:
                        proposicion = self.motor.get_proposicion(nombre_proposicion)
                        if proposicion:
                            print(f"Detalles de la proposición '{nombre_proposicion}':")
                            print(proposicion.descripcion)
                        else:
                            print(f"No se encontró la proposición '{nombre_proposicion}'.")

                elif sub in COMANDOS:
                    info = COMANDOS[sub]
                    print(f"Uso: {info['uso']}")
                    print(info['descripcion'])
                else:
                    print(f"No se reconoce el elemento '{tokens[1]}'.")
                       
            else:
                print("Comandos disponibles:")
                for cmd, info in COMANDOS.items():
                    print(f"  {cmd}: {info['descripcion']}")
        elif verb == 'get':
            if len(tokens) < 2:
                print("Uso: get <tipo> <nombre>")
                return
            tipo = tokens[1].lower()
            nombre = tokens[2] if len(tokens) > 2 else None
            if tipo == 'proposicion':
                proposicion = self.motor.get_proposicion(nombre)
                if proposicion:
                    print(f"Elementos de la proposicion '{nombre}({', '.join(map(str, proposicion.parametros))})':")
                    for elemento in proposicion.elementos:
                        print(f"elemento  {elemento} con atributos{proposicion.elementos[elemento].atributos}")
                else:
                    print(f"No se encontró la proposición '{nombre}'.")
            else:
                print(f"Tipo '{tipo}' no reconocido. Usa get proposicion <nombre>.")
        elif verb == 'acciones':
            acciones = self.motor.get_acciones()
            if acciones:
                print("Acciones disponibles:")
                for accion in acciones:
                    print(f"  {accion.nombre}: {accion.descripcion}")
            else:
                print("No hay acciones disponibles.")
        elif verb == 'proposiciones':
            proposiciones = self.motor.get_proposiciones()
            if proposiciones:
                print("Proposiciones disponibles:")
                for prop in proposiciones:
                    print(f"  {prop.nombre}: {prop.descripcion}")
            else:
                print("No hay proposiciones disponibles.")

        else:
            print(f"Error: comando '{verb}' no reconocido. Usa 'run', 'add' o 'load'.")

    def ejecutar_comando_run(self, prop, params):
        self.motor.ejecutar_accion(prop, params)



    def ejecutar_comando_add(self, prop, params,atributos=None):
        self.motor.add_proposicion(prop, params,atributos)

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
