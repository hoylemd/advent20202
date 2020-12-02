# FILENAME = 'data.txt'
FILENAME = 'test.txt'

with open(FILENAME) as fp:
    items = fp.readlines()


def parse_entry(entry):
    parts = entry[:-1].split(': ')
    password = parts[1]

    policy_parts = parts[0].split(' ')
    range_parts = policy_parts[0].split('-')

    policy = {
        'char': policy_parts[1],
        'min': int(range_parts[0]),
        'max': int(range_parts[1]),
        'raw': parts[0]
    }

    return policy, password


def is_valid(entry):
    policy, password = parse_entry(entry)

    n_c = password.count(policy['char'])

    print(f"char '{policy['char']}' appears {n_c} times in pw {password} ({policy['raw']})")
    if n_c < policy['min']:
        return False

    if n_c > policy['max']:
        return False

    return True


answer = 0

for item in items:
    if is_valid(item):
        answer += 1

print(answer)
