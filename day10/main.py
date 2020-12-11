import fileinput

DEBUG = True


def debug(*args):
    if DEBUG:
        print(*args)


adapters = sorted([int(line) for line in fileinput.input()])

for a in adapters:
    debug(a)

debug(f"max adapter = {adapters[-1] + 3}")

answer = 0


def get_jumps(adapters):
    """Part 1"""
    jolt_jumps = {}
    last_item = 0

    for item in adapters + [adapters[-1] + 3]:
        debug(f"{item=}")

        diff = item - last_item
        jolt_jumps.setdefault(diff, 0)
        jolt_jumps[diff] += 1

        last_item = item

    return jolt_jumps


def count_optional(adapters):
    """Part 2"""
    optional = 0
    last_req = 0

    for i in range(len(adapters)):
        this = adapters[i]
        try:
            next_one = adapters[i + 1]
        except IndexError:
            next_one = this + 3

        if this - last_req < 4 and next_one - last_req < 4:
            debug(f"{this} is optional")
            optional += 1
        else:
            debug(f"{this} is not optional")
            last_req = this

    return optional


answer = 2 ** count_optional(adapters)

debug('---- DEBUG ENDS ----')

print(answer)
