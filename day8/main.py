DEBUG = True

FILENAME = 'test.txt'
# FILENAME = 'data.txt'


def parse_instruction(line):
    op, arg = line.strip().split(' ', 1)
    return op, int(arg)


with open(FILENAME) as fp:
    instructions = [parse_instruction(line) for line in fp.readlines()]

acc = 0
instr_idx = 0
crumbs = set()

while True:
    try:
        instr = instructions[instr_idx]
    except IndexError:
        break

    if DEBUG:
        print(f"{instr=}")

    if instr_idx in crumbs:
        break

    crumbs.add(instr_idx)

    op, arg = instr

    if op == 'acc':
        acc += arg

    if op == 'jmp':
        instr_idx += arg
    else:
        instr_idx += 1

if DEBUG:
    print('---- DEBUG ENDS ----')

print(acc)
