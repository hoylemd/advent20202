DEBUG = True

FILENAME = 'data.txt'
if DEBUG:
    FILENAME = 'test.txt'

with open(FILENAME) as fp:
    items = [line.strip() for line in fp.readlines()]

answer = 0

for item in items:
    if DEBUG:
        print(f"{item=}")
    # --- do work here ---
    pass


print(answer)
