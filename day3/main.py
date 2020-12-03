# FILENAME = 'data.txt'
FILENAME = 'test.txt'

with open(FILENAME) as fp:
    rows = [line.strip() for line in fp.readlines()]

trees = 0
x, y = 0, 0
d_x, d_y = 3, 1

dest_y = len(rows) - 1
n_cols = len(rows[0])
n_wraps = 0
symbol = rows[y][x]

while y < dest_y:
    print(f"{rows[y] * n_wraps}{rows[y][:x]}{symbol}{rows[y][x+1:]}")
    new_x = (x + d_x) % n_cols
    if new_x < x:
        n_wraps += 1

    x = new_x
    y += d_y

    symbol = 'O'
    if rows[y][x] == '#':
        trees += 1
        symbol = 'X'


print(trees)
