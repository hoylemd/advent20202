# FILENAME = 'data.txt'
FILENAME = 'test.txt'

def count_trees(rows, d_x, d_y):
    trees = 0
    x, y = 0, 0

    dest_y = len(rows) - 1
    n_cols = len(rows[0])
    n_wraps = 0
    symbol = rows[y][x]

    while y < dest_y:
        # print(f"{rows[y] * n_wraps}{rows[y][:x]}{symbol}{rows[y][x+1:]}")

        new_x = x + d_x
        if new_x >= n_cols:
            new_x = new_x % n_cols
            n_wraps += 1

        x = new_x
        y += d_y

        symbol = 'O'
        if rows[y][x] == '#':
            trees += 1
            symbol = 'X'

    return trees


with open(FILENAME) as fp:
    rows = [line.strip() for line in fp.readlines()]

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

answer = 1

for d_x, d_y in slopes:
    trees = count_trees(rows, d_x, d_y)

    # print(f"for {d_x}, {d_y}: {trees=}")

    answer *= trees

print(answer)
