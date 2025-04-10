# Skell's Tools (Python Terminal)

Este modulo de python busca convertirse en una libreria que permita manejar de manera estetica aplicaciones de consola/terminal desarrolladas en python con librerias integradas

> Este README sera editado posteriormente para mejorar la documentacion

## Funciones existentes:
- Limpiar() :
    - Permite limpiar la pantalla de la terminal dejandola completamente vacia, es el equivalente a ejecutar 'cls' en la terminal

- tamaño() :
    - Devuelve el "tamaño" (número de caracteres disponibles en ancho y alto) en una tupla

- esperar() :
    - Recicla el "sleep" de la libreria "time" solo que incorporandolo dentro de skell's tools para no tener que importarla por separado

- ir() :
    - Permite cambiar el lugar del Cursor

- ejecutar() :
    - Permite ejecutar un comando de la terminal por parte del desarrollador

- Alinear() :
    - Permite alinear el texto en formatos Izquierda, Centrado y Derecha