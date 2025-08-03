import random

def start_game():
    mat = [[0] * 4 for _ in range(4)]
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")
    add_new_2(mat)
    return mat

def findEmpty(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return i, j
    return None, None

def add_new_2(mat):
    if all(cell != 0 for row in mat for cell in row):
        return

    for _ in range(30):
        r, c = random.randint(0, 3), random.randint(0, 3)
        if mat[r][c] == 0:
            mat[r][c] = 2
            return

    r, c = findEmpty(mat)
    if r is not None:
        mat[r][c] = 2

def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
            if mat[i][j] == 0:
                return 'GAME NOT OVER'

    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1]:
                return 'GAME NOT OVER'
    for j in range(4):
        for i in range(3):
            if mat[i][j] == mat[i+1][j]:
                return 'GAME NOT OVER'
    return 'LOST'

def compress(mat):
    changed = False
    new_mat = [[0]*4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_mat, changed

def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                changed = True
    return mat, changed

def reverse(mat):
    return [row[::-1] for row in mat]

def transpose(mat):
    return [list(row) for row in zip(*mat)]

def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    new_grid, _ = compress(new_grid)
    return new_grid, changed1 or changed2

def move_right(grid):
    reversed_grid = reverse(grid)
    new_grid, changed = move_left(reversed_grid)
    return reverse(new_grid), changed

def move_up(grid):
    transposed = transpose(grid)
    new_grid, changed = move_left(transposed)
    return transpose(new_grid), changed

def move_down(grid):
    transposed = transpose(grid)
    new_grid, changed = move_right(transposed)
    return transpose(new_grid), changed
