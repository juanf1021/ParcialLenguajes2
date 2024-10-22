# Proyecto ANTLR

Este proyecto utiliza ANTLR 4.13.1 para la generación y ejecución de gramáticas en Python. Asegúrate de seguir los siguientes pasos para compilar y ejecutar correctamente los archivos.

## Requisitos

1. **Python 3** instalado en tu sistema.
2. **ANTLR 4.13.1** configurado como classpath.

### Instalación de dependencias

1. Instala el runtime de ANTLR para Python utilizando `pip`:

   ```bash
   pip install antlr4-python3-runtime==4.13.1
   ```

2. Configura el classpath de ANTLR. Puedes verificarlo con el siguiente comando:

   ```bash
   echo $CLASSPATH
   ```

   Asegúrate de que la variable de entorno `$CLASSPATH` apunte correctamente a ANTLR.

## Compilación y ejecución

1. Compila el archivo de gramática `.g4` con ANTLR utilizando el siguiente comando:

   ```bash
   antlr4 -visitor -Dlanguage=Python3 NAME.g4
   ```

   Reemplaza `NAME.g4` por el nombre de tu archivo de gramática.

2. Ejecuta el archivo `main.py` con el archivo de entrada adecuado:

   ```bash
   python3 main.py input.txt
   ```

   Reemplaza `input.txt` por el archivo de texto que deseas procesar.

## Notas

- Asegúrate de que ANTLR esté correctamente configurado en tu sistema antes de compilar el archivo `.g4`.
- Si encuentras problemas al ejecutar los comandos, verifica las versiones de Python y ANTLR instaladas.

