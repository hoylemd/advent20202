DEBUG = True


def debug(*args):
    if DEBUG:
        print(*args)


preamble_length = 5
FILENAME = 'test.txt'
# preamble_length = 25
# FILENAME = 'data.txt'


with open(FILENAME) as fp:
    items = [int(line) for line in fp.readlines()]


def validate_num(num, history):
    debug(f"{num=} {history=}")

    hist = sorted(history)
    left, right = 0, len(history) - 1

    while(left != right and (cand := hist[left] + hist[right]) != num):
        if cand < num:
            left += 1
        else:
            right -= 1

    if left == right:
        return False

    debug(f"{num} = {hist[left]} + {hist[right]}")
    return True


answer = 0
i = preamble_length
while i < len(items):
    item = items[i]
    debug(f"{item=}")

    history = items[i - preamble_length:i]
    if not validate_num(item, history):
        answer = item
        break

    i += 1

debug('---- DEBUG ENDS ----')

print(answer)
