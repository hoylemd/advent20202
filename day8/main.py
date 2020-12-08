DEBUG = False  # True

# FILENAME = 'test.txt'
FILENAME = 'data.txt'


def debug(*args):
    if DEBUG:
        print(*args)


def parse_instruction(line):
    op, arg = line.strip().split(' ', 1)
    return op, int(arg)


with open(FILENAME) as fp:
    instructions = [parse_instruction(line) for line in fp.readlines()]


def run_code(instructions):
    """Part 1"""
    acc = 0
    instr_idx = 0
    crumbs = set()

    while True:
        try:
            instr = instructions[instr_idx]
        except IndexError:
            return acc, None

        debug(f"{instr=}")

        if instr_idx in crumbs:
            return acc, 'loop'

        crumbs.add(instr_idx)

        op, arg = instr

        if op == 'acc':
            acc += arg

        if op == 'jmp':
            instr_idx += arg
        else:
            instr_idx += 1


answer, error = run_code(instructions)

debug('---- DEBUG ENDS ----')

print(answer)
