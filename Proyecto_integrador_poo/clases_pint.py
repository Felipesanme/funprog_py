import readchar
import os
import random

from dataclasses import dataclass


@dataclass
class Juego():

	maze: list = None
	start: tuple = None
	end: tuple = None
	x_pos: int = None
	y_pos: int = None


	def play(self):

		# maze_str = ""
		# for row in range(len(self.maze)):
		# 	maze_str += "".join(self.maze[row]) + "\n"
		# print(maze_str)

		while self.start[0] <= self.y_pos <= self.end[0] and self.start[1] <= self.x_pos <= self.end[
			1]:

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

			maze_str = ""
			for row in range(len(self.maze)):
				maze_str += "".join(self.maze[row]) + "\n"
			print(maze_str)

			if self.y_pos == self.end[0] and self.x_pos == self.end[1] - 1:
				break


@dataclass
class JuegoArchivo(Juego):
	path_maps: str = None
	file_list: list = None
	rand_map: str = None
	path: str = None

	def __init__(self):
		self.__map_select()
		self.__init_coord()
		self.__map_create()

		self.x_pos = self.start[1]
		self.y_pos = self.start[0]

	def __map_select(self):
		self.path_maps = "/Users/felipe/Documents/ADA/FP Python/funprog_py/Proyecto_integrador_poo/Mapas"
		self.file_list = list(filter(lambda f: ".txt" in f, os.listdir(self.path_maps)))
		self.rand_map = random.choice(self.file_list)
		self.path = f"{self.path_maps}/{self.rand_map}"

	def __init_coord(self):
		with open(self.path) as f:
			lines = f.read()
			first_line = lines.split("\n", 1)[0]
			a, b, c, d = list(map(int, first_line.split()))
			self.start = (a, b)
			self.end = (c, d)

	def __map_create(self):
		with open(self.path) as f:  # imprimir con el salto de línea
			next(f)
			self.maze = f.readlines()
			self.maze = [line.strip() for line in self.maze]

		for i in range(len(self.maze)):
			self.maze[i] = list(self.maze[i])


if __name__ == "__main__":
	main()
