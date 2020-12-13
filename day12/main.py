import fileinput

DEBUG = True


def debug(*args):
    if DEBUG:
        print(*args)


heading_components = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0)
}
cardinals = [k for k in heading_components.keys()]


def move_direction(direction, distance, x, y):
    dx, dy = heading_components[direction]
    x += dx * distance
    y += dy * distance

    return x, y


def turn(direction, distance, heading):
    steps = int(distance / 90)

    if direction == 'L':
        steps *= -1

    idx = (cardinals.index(heading) + steps) % len(cardinals)
    return cardinals[idx]


def execute(course):
    """Part 1"""
    x, y = 0, 0
    heading = 'E'

    for item in course:
        nx, ny = x, y
        n_heading = heading
        instr, arg = item[0], int(item[1:])

        if instr == 'F':
            instr = heading

        if instr in heading_components:
            nx, ny = move_direction(instr, arg, x, y)

        if instr in ['R', 'L']:
            n_heading = turn(instr, arg, heading)

        debug(f"{x}, {y}, {heading} -> {item}({instr} {arg}) -> {nx}, {ny}, {n_heading}")

        x, y = nx, ny
        heading = n_heading

    return x, y


def rotate_right(x, y):
    return -y, x


def rotate_waypoint(direction, distance, x, y):
    steps = int(distance / 90)

    if direction == 'L':
        steps *= -1

    steps = steps % 4

    for i in range(steps):
        x, y = rotate_right(x, y)

    return x, y


def execute_waypoints(course):
    """Part 2"""
    x, y = 0, 0
    wx, wy = 10, -1

    for item in course:
        instr, arg = item[0], int(item[1:])

        if instr == 'F':
            for i in range(arg):
                x += wx
                y += wy

        if instr in heading_components:
            wx, wy = move_direction(instr, arg, wx, wy)

        if instr in ['R', 'L']:
            wx, wy = rotate_waypoint(instr, arg, wx, wy)

    return x, y


def manhattan_distance(x, y):
    debug(f"mann: {x} {y}")
    if x < 0:
        x *= -1

    if y < 0:
        y *= -1

    return x + y


course = [line.strip() for line in fileinput.input()]

x, y = execute_waypoints(course)
answer = manhattan_distance(x, y)

debug('---- DEBUG ENDS ----')

print(answer)
