# FILENAME = 'data.txt'
FILENAME = 'test.txt'

with open(FILENAME) as fp:
    items = fp.readlines()

expenses = sorted(int(item)for item in items)


def find_pair(expenses, left=0, right=-1, offset=0):
    right = len(expenses) - 1
    while (total := expenses[left] + expenses[right] + offset) != 2020:
        if left >= right:
            return None

        if total < 2020:
            left += 1

        if total > 2020:
            right -= 1

    print(f"found pair summing to 2020 with offset: {expenses[left]} + {expenses[right]} + {offset} = {total}")
    return (left, right)


def find_trio(expenses):
    mid = 1
    while mid < len(expenses):
        trimmed = expenses[0:mid] + expenses[mid+1:]
        result = find_pair(trimmed, offset=expenses[mid])
        if result is not None:
            break
        mid += 1

    left, right = result
    if left >= mid:
        left += 1
    if right >= mid:
        right += 1

    return left, mid, right


left, mid, right = find_trio(expenses)

total = expenses[left] + expenses[mid] + expenses[right]
answer = expenses[left] * expenses[mid] * expenses[right]
print(f"{left=}({expenses[left]}) + {right=}({expenses[right]}) + {mid=}({expenses[mid]}) = {total}")

print(answer)
