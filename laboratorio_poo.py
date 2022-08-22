from dataclasses import dataclass


@dataclass
class Vector:
	arreglo: list

	def __add__(self, other):
		res = [self.arreglo[i] + other.arreglo[i] for i in range(len(self.arreglo))]
		return res

	def __sub__(self, other):
		res = [self.arreglo[i] - other.arreglo[i] for i in range(len(self.arreglo))]
		return res

	def __mul__(self, other):
		res = [self.arreglo[i] * other.arreglo[i] for i in range(len(self.arreglo))]
		return res

	def __matmul__(self, other):
		matmul = 0
		for i in range(len(self.arreglo)):
			res = self.arreglo[i] * other.arreglo[i]
			matmul += res
		return matmul

	def __getitem__(self, llave):
		return self.arreglo[llave]

	def __setitem__(self, llave, nuevo):
		self.arreglo[llave] = nuevo

	def __str__(self):
		return str(self.arreglo)


# creando los vectores
vector1 = Vector([2, 2, 2, 2])
vector2 = Vector([7, 8, 9, 11])
print(vector1)
print(vector2)

# Prueba métodos

suma = vector1 + vector2
print(suma)
resta = vector1 - vector2
print(resta)
mult = vector1 * vector2
print(mult)
matmul = vector1 @ vector2
print(matmul)
getitem = vector2[3]
print(getitem)
vector2[3] = 32
print(vector2)