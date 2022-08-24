import os
import random


# f = open("Mapas/map1.txt","r")
# lineas = f.readlines()
# print(lineas)
# f.close()

# with open("Mapas/map1.txt","r") as f: #imprimir con el satlo de línea
# 	for line in f.readlines():
# 		print(line.strip())
maze =[]
ruta_dir_mapas = "/Users/felipe/Documents/ADA/FP Python/funprog_py/Proyecto_integrador_poo/Mapas"
lista_archivos = filter(lambda f: ".txt" in f,os.listdir(ruta_dir_mapas))
print(lista_archivos)
mapa_rand = random.choice(lista_archivos)
path = f"{ruta_dir_mapas}/{mapa_rand}"

with open(path,"r") as f: #imprimir con el salto de línea

	for line in f.readlines()[1:]:
		maze= line.strip("\n")
		print(line.strip())


# with open(path) as f2:
# 	lines = f2.read()
# 	first = lines.split("\n",1)[0]
# 	second = lines.split("\n",2)
# print(first)
# print(second)

# print (path)