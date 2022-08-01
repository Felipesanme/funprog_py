import readchar

k = readchar.readkey()

def dir(k) -> str:

  dic_flechas = {readchar.key.UP: "Arriba", readchar.key.DOWN: "Abajo", readchar.key.LEFT: "Izquierda",
                readchar.key.RIGHT: "Derecha"}

  print(dic_flechas.get(k))

dir(k)
