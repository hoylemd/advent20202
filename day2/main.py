# FILENAME = 'data.txt'
FILENAME = 'test.txt'

with open(FILENAME) as fp:
    items = fp.readlines()


def parse_entry(entry):
    pass


def is_valid(entry):
    policy, password = parse_entry(entry)


answer = 0

for item in items:
    if is_valid(item):
        answer += 1

print(answer)
