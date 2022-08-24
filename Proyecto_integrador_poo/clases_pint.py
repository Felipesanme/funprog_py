import readchar
import os
import random

from dataclasses import dataclass


@dataclass
class Juego():

	maze: list
	start: tuple
	end: tuple
	x_pos: int
	y_pos: int

	def play(self):

		while self.start[0] <= self.y_pos <= self.end[0] and self.start[1] <= self.x_pos <= self.end[1]:
			tecla = readchar.readkey()

			dic_keys = {readchar.key.UP: "Arriba", readchar.key.DOWN: "Abajo",
						   readchar.key.LEFT: "Izquierda", readchar.key.RIGHT: "Derecha"}

			if self.y_pos == (self.end[0] - 1) and self.x_pos == (self.end[1] - 2):
				break

			if dic_keys.get(tecla) == "Arriba" and self.maze[self.y_pos - 1][self.x_pos] != "#":
				self.y_pos -= 1
				self.maze[self.y_pos + 1][self.x_pos] = "."

			elif dic_keys.get(tecla) == "Abajo" and self.maze[self.y_pos + 1][self.x_pos] != "#":
				self.y_pos += 1
				self.maze[self.y_pos - 1][self.x_pos] = "."

			elif dic_keys.get(tecla) == "Izquierda" and self.maze[self.y_pos][self.x_pos - 1] != "#":
				self.x_pos -= 1
				self.maze[self.y_pos][self.x_pos + 1] = "."

			elif dic_keys.get(tecla) == "Derecha" and self.maze[self.y_pos][self.x_pos + 1] != "#":
				self.x_pos += 1
				self.maze[self.y_pos][self.x_pos - 1] = "."

			else:
				self.maze[self.y_pos][self.x_pos] = "p"

			self.maze[self.y_pos][self.x_pos] = "p"

			os.system('cls' if os.name == 'nt' else 'clear')

			self.maze = ""
			for row in range(len(self.maze)):
				maze += "".join(self.maze[row]) + "\n"
			print(self.maze)

			if self.y_pos == self.end[0] and self.x_pos == self.end[1] - 1:
				break

@dataclass
class JuegoArchivo(Juego):

	path_maps: str
	file_list: list
	rand_map: str
	path: str

	def map_select(self):

		self.path_maps = "/Users/felipe/Documents/ADA/FP Python/funprog_py/Proyecto_integrador_poo/Mapas"
		self.file_list = list(filter(lambda f: ".txt" in f, os.listdir(self.path_maps)))
		self.rand_map = random.choice(self.file_list)
		self.path = f"{self.path_maps}/{self.rand_map}"

	def init_coord(self, juego: Juego):

		with open(self.path) as f:
			lines = f.read()
			first_line = lines.split("\n", 1)[0]
			a, b, c, d = list(map(int, first_line.split()))
			juego.start = (a, b)
			juego.end = (c, d)

	def map_create(self, juego: Juego):

		with open(self.path) as f:  # imprimir con el salto de línea
			next(f)
			juego.maze = f.readlines()
			juego.maze = [line.strip() for line in maze]

		for i in range(len(juego.maze)):
			juego.maze[i] = list(juego.maze[i])

if __name__ == "__main__":
	main()
