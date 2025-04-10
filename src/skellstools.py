# Librerías integradas necesarias
import ctypes.wintypes
import os
import sys
import ctypes
import msvcrt
import argparse
from time import sleep
from enum import Enum

# Configuración de la API de Windows
kernel32 = ctypes.windll.kernel32
STD_OUTPUT_HANDLE = -11

#Lista de Colores disponibles en la consola de Windows en una clase
class Color(Enum):
    #Codigos
    NEGRO = 0x00
    AZUL = 0x01
    VERDE = 0x02
    CYAN = 0x03
    ROJO = 0x04
    MAGENTA = 0x05
    AMARILLO = 0x06
    BLANCO = 0x07
    GRIS = 0x08

#Configuracion Inicial de la Consola
handle = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

#Funciones para el manejo de la consola

# Funcion para esperar 1 segundo o mas
def esperar(segundo):
    sleep(segundo)

# Limpia la consola dejandola completamente vacia
def limpiar():
    os.system('cls')

# Devolver el tamaño de la Terminal
def tamaño():
    z = os.get_terminal_size()
    return (z.columns, z.lines)

# Funcion que permite cambiar la posicion del cursor de la terminal
def ir(x, y):
    kernel32.SetConsoleCursorPosition(handle, ctypes.wintypes._COORD(x, y))

# Funcion que permite ejecutar un comando del Sistema especificado por el desarrollador/usuario
def ejecutar(comando, mostrar=True):
    with os.popen(comando) as proceso:
        salida = proceso.read()
    if mostrar:
        print(salida)
    return(salida)