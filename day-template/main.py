import fileinput

DEBUG = True


def debug(*args):
    if DEBUG:
        print(*args)


lines = [line.strip() for line in fileinput.input()]

answer = 0

for item in lines:
    debug(f"{item=}")
    # --- do work here ---
    pass

debug('---- DEBUG ENDS ----')

print(answer)
