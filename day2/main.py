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
        '1st': int(range_parts[0]) - 1,
        '2nd': int(range_parts[1]) - 1,
        'raw': parts[0]
    }

    return policy, password


def is_valid(entry):
    policy, password = parse_entry(entry)

    print(
        f"expecting '{policy['char']}' to appear at index {policy['1st']} XOR {policy['2nd']} "
        f"in pw {password} ({policy['raw']})"
    )

    c1 = password[policy['1st']]
    c2 = password[policy['2nd']]
    if (
        c1 == policy['char']
        and c2 != policy['char']
    ) or (
        c1 != policy['char']
        and c2 == policy['char']
    ):
        return True

    return False


answer = 0

for item in items:
    if is_valid(item):
        answer += 1

print(answer)
