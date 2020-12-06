DEBUG = True

FILENAME = 'test.txt'
# FILENAME = 'data.txt'

with open(FILENAME) as fp:
    lines = [line.strip() for line in fp.readlines()]

answer = 0

affirmatives = set()

for line in lines:
    if DEBUG:
        print(f"{line=}")

    if not line:
        if DEBUG:
            print(f"Group complete: {affirmatives=}({len(affirmatives)})")
        answer += len(affirmatives)
        if DEBUG:
            print(f"{answer=}")
        affirmatives = set()
        continue

    affirmatives |= set(line)


if DEBUG:
    print(f"Group complete: {affirmatives=}({len(affirmatives)})")
answer += len(affirmatives)
if DEBUG:
    print(f"{answer=}")

if DEBUG:
    print('---- DEBUG ENDS ----')

print(answer)
