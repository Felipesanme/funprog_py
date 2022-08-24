import os
import random

maze =[]
ruta_dir_mapas = "/Users/felipe/Documents/ADA/FP Python/funprog_py/Proyecto_integrador_poo/Mapas"
lista_archivos = list(filter(lambda f: ".txt" in f,os.listdir(ruta_dir_mapas)))

mapa_rand = random.choice(lista_archivos)
path = f"{ruta_dir_mapas}/{mapa_rand}"

with open (path) as f:
	lineas = f.read()
	primera_linea = lineas.split("\n",1)[0]
	px_inicial, py_inicial, px_final, py_final = list(map(int,primera_linea.split()))


print(primera_linea)
print (px_inicial, py_inicial, px_final,py_final)
with open(path) as f: #imprimir con el salto de línea
	next(f)
	maze = f.readlines()
	maze = [line.strip() for line in maze]
print (maze)

for i in range(len(maze)):
	maze[i] = list(maze[i])

print (maze)