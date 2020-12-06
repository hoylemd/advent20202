DEBUG = False  # True

# FILENAME = 'test.txt'
FILENAME = 'data.txt'

with open(FILENAME) as fp:
    lines = [line.strip() for line in fp.readlines()]

answer = 0
affirmatives = None

for line in lines:
    if DEBUG:
        print(f"{line=}")

    if not line:
        if DEBUG:
            print(f"Group complete: {affirmatives=}({len(affirmatives)})")
        answer += len(affirmatives)
        if DEBUG:
            print(f"{answer=}")
        affirmatives = None
        continue

    if affirmatives is None:
        affirmatives = set(line)
    else:
        affirmatives &= set(line)


if DEBUG:
    print(f"Group complete: {affirmatives=}({len(affirmatives)})")
answer += len(affirmatives)
if DEBUG:
    print(f"{answer=}")

if DEBUG:
    print('---- DEBUG ENDS ----')

print(answer)
