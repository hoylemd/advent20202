DEBUG = True


def debug(*args):
    if DEBUG:
        print(*args)


prefix = 5
FILENAME = 'test.txt'
# prefix = 25
# FILENAME = 'data.txt'


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


def find_crack(items, prefix):
    """Part 1"""
    answer = 0
    i = prefix
    while i < len(items):
        item = items[i]
        debug(f"{item=}")

        history = items[i - prefix:i]
        if not validate_num(item, history):
            answer = item
            break

        i += 1

    return answer


with open(FILENAME) as fp:
    items = [int(line) for line in fp.readlines()]

answer = find_crack(items, prefix)

debug('---- DEBUG ENDS ----')

print(answer)
