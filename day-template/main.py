DEBUG = True


def debug(*args):
    if DEBUG:
        print(*args)


FILENAME = 'test.txt'
# FILENAME = 'data.txt'

with open(FILENAME) as fp:
    items = [line.strip() for line in fp.readlines()]

answer = 0

for item in items:
    debug(f"{item=}")
    # --- do work here ---
    pass

debug('---- DEBUG ENDS ----')

print(answer)
