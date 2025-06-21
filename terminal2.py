#!/usr/bin/env python3
import sys



class Terminal:
    """
    Version complicada, DESCARTAR
    """
    def __init__(self, motor):

        self.motor = motor
        # Aquí podrías inicializar más cosas si es necesario
       
    def _split_params(self, params_str):
        """
        Divide params_str en lista de parámetros separando por comas que no estén dentro de comillas.
        Mantiene comillas para luego limpiarlas.
        """
        params = []
        current = ''
        in_quote = False
        quote_char = ''
        for ch in params_str:
            if ch in ('"', "'"):
                if not in_quote:
                    in_quote = True
                    quote_char = ch
                elif quote_char == ch:
                    in_quote = False
                current += ch
            elif ch == ',' and not in_quote:
                params.append(current.strip())
                current = ''
            else:
                current += ch
        if current:
            params.append(current.strip())
        # Limpiar comillas exteriores
        cleaned = []
        for p in params:
            if len(p) >= 1 and ((p[0] == '"' and p[-1] == '"') or (p[0] == "'" and p[-1] == "'") or (p[0] == '“' and p[-1] == '”')):
                cleaned.append(p[1:-1])
            else:
                # Si no tiene comillas, entonces debe ser un numero int
                try:
                    p = int(p)
                except ValueError:
                    raise ValueError(f"Parámetro inválido: {p}. Debe ser un número entero o una cadena entre comillas.")
                
                cleaned.append(p)
        return cleaned

    
    def procesar_linea(self, linea_raw):
        # 1) Eliminar comentarios
        linea = linea_raw.split('//', 1)[0].strip()
        if not linea:
            return

        # 2) Manejar 'exit' o 'quit'
        if linea.lower() in ('exit', 'exit;'):
            sys.exit(0)


        # 3) Verificar comando, lo guarda y extraer llamada
        partes = linea.strip().split(None, 1)  # Separa por el primer espacio
        if len(partes) < 2:
            print("Error: formato incorrecto. Usa '<comando> <llamada>;'.")
            return
        comando, llamada = partes[0], partes[1]
        if comando not in ('run', 'new', 'add', 'load'):
            print("Error: comando no reconocido. Usa 'run', 'new' o 'add'.")
            return

        #llamada = llamada[:-1].strip()
        if not llamada:
            print("Error: llamada vacía.")
            return

        if comando == 'load':
            # 4) Cargar archivo
            if not llamada:
                print("Error: falta el nombre del archivo.")
                return
            self.motor.set_archivo(llamada)
            self.motor.cargar_archivo()
            return

        # 5) Separar nombre de comando y parámetros
        try:
            idx1 = llamada.index('(')
            idx2 = llamada.rindex(')')
        except ValueError:
            print("Error de sintaxis: falta paréntesis.")
            return

        prop = llamada[:idx1].strip()
        params_str = llamada[idx1+1:idx2].strip()

        # 6) Dividir parámetros por comas y limpiar comillas
        try:
            params = self._split_params(params_str) if params_str else []
        except Exception as e:
            print(f"Error al procesar parámetros: {e}")
            return

        # 7) Despachar comando
        if comando == 'run':
            self.ejecutar_comando_run(prop, params)
        elif comando == 'new':
            self.ejecutar_comando_new(prop, params)
        elif comando == 'add':
            self.ejecutar_comando_add(prop, params)

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


