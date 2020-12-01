with open('data.txt') as fp:
    items = fp.readlines()

expenses = sorted(int(item)for item in items)

left = 0
right = -1

while total := expenses[left] + expenses[right] != 2020:
    if total < 2020:
        left += 1

    if total > 2020:
        left -= 1


print(expenses[left] * expenses[right])
