# FILENAME = 'data.txt'
FILENAME = 'test.txt'

with open(FILENAME) as fp:
    items = fp.readlines()

answer = 0

for item in items:
    # --- do work here ---
    pass


print(answer)
