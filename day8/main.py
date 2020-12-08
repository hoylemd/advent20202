DEBUG = True

FILENAME = 'test.txt'
# FILENAME = 'data.txt'

with open(FILENAME) as fp:
    items = [line.strip() for line in fp.readlines()]

answer = 0

for item in items:
    if DEBUG:
        print(f"{item=}")
    # --- do work here ---
    pass

if DEBUG:
    print('---- DEBUG ENDS ----')

print(answer)
