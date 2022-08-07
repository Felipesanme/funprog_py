import readchar
import os

maze='''p.#######################
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

mat_maze=[]

def clean_screen_show(maze:str)->list:

    os.system('cls' if os.name == 'nt' else 'clear')

    print(maze)

    mat_maze = list(maze.split("\n"))

    for i in range(len(mat_maze)):
        mat_maze[i] = list(mat_maze[i])
    return(mat_maze)

px = 0
py = 0
start = (px,py)
end = (len(clean_screen_show(maze)),len(clean_screen_show(maze)))

def main_loop (px,py,start,end,mat_maze):

    while start[0] <= py <= end[0] and start[1] <= px <= end[1]:
        tecla = readchar.readkey()

        dic_flechas = {readchar.key.UP: "Arriba", readchar.key.DOWN: "Abajo",
                       readchar.key.LEFT: "Izquierda", readchar.key.RIGHT: "Derecha"}

        if py == (end[0] - 1) and px == (end[1] - 2):
            break

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

        # print(py,px)

        maze=""
        for row in range(len(mat_maze)):
            maze += "".join(mat_maze[row]) + "\n"
        print(maze)

        if py == end[0] and px == end[1] - 1:
            break

def main():

    clean_screen_show(maze)
    main_loop(px,py,start,end,clean_screen_show(maze))

if __name__ == "__main__":
    main()
