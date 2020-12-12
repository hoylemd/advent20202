import fileinput

DEBUG = False


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


def accumulate_paths(adapters):
    """Part 2"""
    adapters = [0] + adapters
    queue = [0]
    paths = [0] * len(adapters)
    seen = set()

    paths[0] = 1

    while queue:
        debug(f"{queue=}")
        debug(f"{paths=}")
        debug(f"{seen=}")

        top = queue[0]
        queue = queue[1:]
        i = 0
        for node in adapters:
            diff = node - adapters[top]

            debug(f"{node} - {adapters[top]} = {diff}")
            if diff > 0 and diff < 4:
                paths[i] += paths[top]
                if node not in seen:
                    debug(f"adding {node} to seen")
                    queue.append(i)
                    seen.add(node)
            i += 1
        debug()
    return paths[-1]


answer = accumulate_paths(adapters)

debug('---- DEBUG ENDS ----')

print(answer)
