# TFG
# Motor de reglas interactivo

Este proyecto contiene un prototipo de motor de reglas escrito en Python.
Para ejecutarlo se utiliza `main.py`, que ofrece algunos argumentos
opcionales.

```
python main.py [opciones]
```

## Argumentos disponibles

- `--log-level` establece el nivel de detalle de los mensajes de log.
  Valores permitidos: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.
  El valor por defecto es `INFO`.
- `--log-file` permite indicar una ruta de fichero donde se guardarán los
  mensajes de log. Si se omite este argumento los logs solo se muestran por
  pantalla.
## Terminal interactiva

Al ejecutar `main.py` se inicia una terminal que permite interactuar con el
motor. Algunos comandos básicos son:

- `load <archivo>`: carga un archivo de reglas o proposiciones.
- `run <accion> [param1] [param2] ...`: ejecuta una acción del motor.
- `add <proposicion> [param1] [param2] ... <atributo>:<valor> ...`: añade una
  proposición con parámetros y atributos.
- `get proposicion <nombre>`: muestra los elementos de la proposición
  indicada.
- `reset`: elimina todas las reglas y proposiciones cargadas.
- `exit`/`quit`: cierra la aplicación.
- `help [comando]`: muestra información de ayuda general o sobre un comando
  concreto.
  
## Ejemplo de sesión

A continuación se muestra una sesión de ejemplo. Primero se inicia el programa
sin argumentos. En la terminal interactiva se carga el archivo
`iteracion4.txt` y se ejecutan algunas acciones:

```bash
$ python main.py
> load caso_de_uso4.txt
> acciones           # lista las acciones disponibles
> run MostrarUsuarios
> run MostrarLibros
> run PrestarLibro Nacho "El Quijote"
```

Con `load` se leen las reglas y proposiciones definidas en el fichero. El
comando `acciones` permite ver las acciones que se han cargado. Los comandos
`run` ejecutan la acción indicada con los parámetros proporcionados.
