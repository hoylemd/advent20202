import fileinput

DEBUG = True


def debug(*args):
    if DEBUG:
        print(*args)


lines = [line.strip() for line in fileinput.input()]

mask = lines.pop(0).split(' ')[-1]


def parse_instruction(line):
    parts = line.split('] = ', 1)
    val = int(parts[-1])
    location = int(parts[0][4:])

    return location, val


def apply_mask(mask, value):
    return value


answer = 0
memory = {}

debug(f"{mask=}")
for line in lines:
    l, v = parse_instruction(line)
    debug(f"Set memory location {l} to {v}")

    memory[l] = apply_mask(mask, v)

answer = sum(memory.values())

debug('---- DEBUG ENDS ----')

print(answer)
