from random import shuffle, randrange


def make_maze(w=16, h=8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["#  "] * w + ['#'] for _ in range(h)] + [[]]
    hor = [["###"] * w + ['#'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                hor[max(y, yy)][x] = "#  "
            if yy == y:
                ver[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    maze = ""
    for (a, b) in zip(hor, ver):
        maze += ''.join(a + ['\n'] + b + ['\n'])
    maze = maze.split('\n')
    maze = [x for x in maze if x != '']
    return maze


def add_word(maze, word='TESTICLES'):
    x = len(maze[0])
    y = len(maze)
    for letter in word:
        added = False
        while not added:
            rx = randrange(x)
            ry = randrange(y)
            print(rx, ry)
            if maze[ry][rx] == ' ':
                print(letter)
                tmp = list(maze[ry])
                tmp[rx] = letter
                maze[ry] = ''.join(tmp)
                added = True
    return maze


if __name__ == '__main__':
    maze = make_maze()
    print('\n'.join(maze))
    print('\n'.join(add_word(maze)))
