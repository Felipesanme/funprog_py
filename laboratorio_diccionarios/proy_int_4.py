import readchar
import os
os.system('cls' if os.name == 'nt' else 'clear')
maze = '''..#######################
......#.....#.#.....#...#
#.#######.###.#####.###.#
#...............#.......#
#.#####.###.#####.#.#.###
#.#.....#.#.#.....#.#...#
#.###.###.#####.#######.#
#.#.....#.........#...#.#
#.#.#.#####.#######.###.#
#.#.#.#.#.....#.#.#.....#
#.###.#.#######.#.#.#.#.#
#...#.#.......#.....#.#.#
#####.#.#.#####.#######.#
#.......#.#.......#.....#
#####.###.###.#####.#.#.#
#.....#...#...#...#.#.#.#
#####.#.###.###.###.###.#
#.#...#.........#...#.#.#
#.#.#.#.###.#####.###.###
#...#.#...#...#.....#...#
#.###.#.#.#####.###.#.###
#...#.#.#.#...#...#.#...#
#####.#######.#.###.#.#.#
#.......#.......#.....#.#
#######################.#'''

print(maze)

mat_maze = list(maze.split("\n"))

# print(mat_maze)
# print(len(mat_maze))

for i in range(len(mat_maze)):
    mat_maze[i] = list(mat_maze[i])

px = 0
py = 0
player_pos = [px, py]
start = (px,py)
end = (len(mat_maze),len(mat_maze))

while start[0] <= py <= end[0] and start[1] <= px <= end[1]:
    tecla = readchar.readkey()

    dic_flechas = {readchar.key.UP: "Arriba", readchar.key.DOWN: "Abajo",
                   readchar.key.LEFT: "Izquierda", readchar.key.RIGHT: "Derecha"}

    if dic_flechas.get(tecla) == "Arriba" and mat_maze[py-1][px] != "#":
        py -= 1
        mat_maze[py+1][px] = "."
    elif dic_flechas.get(tecla) == "Abajo" and mat_maze[py + 1][px] != "#":
        py += 1
        mat_maze[py-1][px] = "."
    elif dic_flechas.get(tecla) == "Izquierda" and mat_maze[py][px - 1] != "#":
        px -= 1
        mat_maze[py][px+1] = "."
    elif dic_flechas.get(tecla) == "Derecha" and mat_maze[py][px + 1] != "#":
        px += 1
        mat_maze[py][px-1] = "."
    else:
        mat_maze [py][px] = "p"

    mat_maze [py][px] = "p"
    os.system('cls' if os.name == 'nt' else 'clear')
    print(py,px)
    # print(mat_maze)

    maze=""
    for row in range(len(mat_maze)):
        maze += "".join(mat_maze[row]) + "\n"
    print(maze)


    # maze = sep.join(mat_maze)


#
# def main():
#
#     clean_screen(0)
#
# if __name__ == "__main__":
#     main()