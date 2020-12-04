# FILENAME = 'data.txt'
FILENAME = 'test.txt'

DEBUG = True

with open(FILENAME) as fp:
    items = fp.readlines()

answer = 0

for item in items:
    if DEBUG:
        print(f"{item=}")
    # --- do work here ---
    pass


print(answer)
