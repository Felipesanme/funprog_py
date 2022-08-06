import readchar
import os
os.system('cls' if os.name == 'nt' else 'clear')
maze = '''..###################
....#...#...........#
#.###.#.#.#.#.###.#.#
#.#...#.#.#.#.#...#.#
#.#.###.#.#####.#####
#.....#.#.#...#...#.#
###.#####.###.#.###.#
#.........#.....#...#
#.###########.#####.#
#.#...#.....#...#...#
#####.###.#.###.#.###
#.....#...#.#...#...#
#.###.###.#####.#.###
#.#...#.#...#.......#
#.#####.#.#########.#
#.......#...#.......#
#.#####.###.#.#####.#
#...#.........#...#.#
###.###.###.###.#.#.#
#.....#.#.....#.#...#
###################.#'''

print(maze)

mat_maze = list(maze.split("\n"))

for i in range(len(mat_maze)):
    mat_maze[i] = list(mat_maze[i])



tecla = readchar.readkey()
px = 0
py = 0
player_pos = [px, py]
start = (0,0)
end = (len(mat_maze),len(mat_maze))


def direction(tecla, mat_maze, px, py):

    dic_flechas = {readchar.key.UP: mat_maze[px][py - 1], readchar.key.DOWN: mat_maze[px][py + 20],
                   readchar.key.LEFT: mat_maze[px - 1][py], readchar.key.RIGHT: mat_maze[px + 1][py]
                   }

    print(dic_flechas.get(tecla))

direction(tecla, mat_maze, px, py)
#
# def clean_screen(n:int):
#     k = readchar.readkey()
#     cont = 1
#     while cont <= 50:
#         k = readchar.readkey()
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print(cont)
#         cont += 1
#     os.system('cls' if os.name == 'nt' else 'clear')
#
# def main():
#
#     clean_screen(0)
#
# if __name__ == "__main__":
#     main()