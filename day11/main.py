import fileinput

DEBUG = False


def debug(*args):
    if DEBUG:
        print(*args)


lobby = [line.strip() for line in fileinput.input()]

answer = 0


def debug_lobby(lobby):
    debug('\n'.join(lobby))


adj_adjs = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),           (1, 0),
    (-1, 1),  (0, 1),  (1, 1)
]


def update_cell(lobby, x, y):
    state = lobby[y][x]
    if state == '.':
        return state, False

    occupied = 0
    for dx, dy in adj_adjs:
        t_x = x + dx
        t_y = y + dy

        if t_x < 0 or t_y < 0:
            continue

        try:
            t_v = lobby[t_y][t_x]
        except IndexError:
            continue

        if t_v == '#':
            occupied += 1

    if state == 'L' and occupied == 0:
        return '#', True

    if state == '#' and occupied > 3:
        return 'L', True

    return state, False


def update_lobby(lobby):
    changed = False
    new_lobby = []
    y = 0
    for row in lobby:
        x = 0
        new_row = []
        for cell in row:
            new_cell, cell_changed = update_cell(lobby, x, y)
            new_row.append(new_cell)
            changed |= cell_changed
            x += 1

        new_lobby.append(''.join(new_row))
        y += 1

    return new_lobby, changed


def count_seats(lobby):
    return sum(row.count('#') for row in lobby)


def stabilize_and_count_seats(lobby):
    i = 0
    changed = True
    while changed:
        debug(f"step {i + 1}:")
        debug_lobby(lobby)
        lobby, changed = update_lobby(lobby)
        debug()
        i += 1

    return count_seats(lobby)


debug('---- DEBUG ENDS ----')

print(stabilize_and_count_seats(lobby))
