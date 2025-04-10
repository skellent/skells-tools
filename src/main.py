from skellstools import limpiar, tamaño

print("Este texto desaparecera y no sera visualizado")
limpiar()
print("Este texto si sera visible y seguido del process finished aparecera la barra de comandos del usuario")
print("Ahora observa el tamano de tu terminal abierta: ")
print(f"Alto: {tamaño()[0]}")
print(f"Ancho: {tamaño()[1]}")