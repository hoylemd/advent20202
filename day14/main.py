import fileinput

DEBUG = False


def debug(*args):
    if DEBUG:
        print(*args)


def parse_instruction(line):
    parts = line.split('] = ', 1)
    val = int(parts[-1])
    location = int(parts[0][4:])

    return location, val


def print_bin_num(num, width):
    binny = f"{num:b}"
    padding = width - len(binny)

    return f"{'0' * padding}{binny} = {num}"


def apply_mask(mask, value):
    debug(f"applying mask to {value}")
    width = len(mask)
    t_mask = int(mask.replace('X', '0'), 2)
    f_mask = int(mask.replace('X', '1'), 2)

    debug(mask)
    debug(print_bin_num(value, width))
    debug(print_bin_num(t_mask, width))
    debug(print_bin_num(f_mask, width))

    value = value | t_mask
    value = value & f_mask

    debug(print_bin_num(value, width))

    return value


lines = [line.strip() for line in fileinput.input()]

answer = 0
memory = {}

for line in lines:
    if line.startswith('mask'):
        mask = line.split(' ')[-1]
        continue

    l, v = parse_instruction(line)

    masked = apply_mask(mask, v)
    debug(f"Set memory location {l} to {masked}")

    memory[l] = masked

answer = sum(memory.values())

debug('---- DEBUG ENDS ----')

print(answer)
