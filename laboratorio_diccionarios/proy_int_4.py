import readchar
import os

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

# for row in mat_maze:
#     print(row)


# print(mat_maze[20][20])
# print(len(mat_maze))

key = readchar.readkey()
coord_x = 0
coord_y = 0
player_pos = [coord_x, coord_y]

def direction(k) -> str:

  move_up = mat_maze[coord_x][coord_y - 1]
  move_down = mat_maze[coord_x][coord_y + 1]
  move_right = mat_maze[coord_x + 1][coord_y]
  move_left = mat_maze[coord_x - 1][coord_y]

  dic_flechas = {readchar.key.UP: move_up, readchar.key.DOWN: move_down, readchar.key.LEFT: move_left,
                readchar.key.RIGHT: move_right}

  print(dic_flechas.get(key))

direction(key)
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