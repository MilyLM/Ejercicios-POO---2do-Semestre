# Ejercicio 9: Manejo de Archivos y Metadatos con Python

Este proyecto explora la interacción de Python con el sistema de archivos del sistema operativo mediante el módulo `os`. El objetivo principal es la creación, manipulación y análisis de archivos de texto, incluyendo el cálculo de su peso en disco.

## Funcionalidades

* **Creación Dinámica:** Generación de archivos de texto (`.txt`) mediante scripts de Python.
* **Escritura de Datos:** Inserción de contenido específico en archivos existentes.
* **Análisis de Metadatos:** Obtención del tamaño exacto de los archivos en bytes.
* **Conversión de Unidades:** Lógica para transformar el peso de los archivos a Kilobytes (KB) y Megabytes (MB).

## Estructura del Código

El ejercicio consta de los siguientes scripts:
* `add.py`: Script encargado de generar o añadir información a archivos.
* `Escritura.py`: Enfocado en la edición y guardado de contenido de texto.
* `filesize.py`: Script principal que utiliza `os.path.getsize` para calcular y mostrar el tamaño del archivo en consola.
* `test.txt`: Archivo generado durante las pruebas para validar los cálculos.

## Resultados de la Simulación

En la terminal se observa el cálculo preciso:
1. Se genera un archivo de prueba.
2. El script identifica un tamaño de **1024.00 KB**.
3. Se realiza la conversión exitosa a **1.0 MB**.

---
*Desarrollado por Mily - 2do Semestre*