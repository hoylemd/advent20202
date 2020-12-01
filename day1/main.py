with open('data.txt') as fp:
    items = fp.readlines()

expenses = sorted(int(item)for item in items)


def find_pair(expenses, left=0, right=-1, offset=0):
    while (total := expenses[left] + expenses[right] + offset) != 2020:
        if total < 2020:
            left += 1

        if total > 2020:
            right -= 1

    return left, right


left, right = find_pair(expenses)

print(expenses[left] * expenses[right])
