# FILENAME = 'data.txt'
FILENAME = 'test.txt'

DEBUG = False

with open(FILENAME) as fp:
    lines = fp.readlines()


def gen_passports(lines):
    pport = {}
    for line in lines:
        trimmed = line.strip()

        if trimmed == '':
            yield pport
            pport = {}
            continue

        for field in trimmed.split(' '):
            k, v = field.split(':')
            pport[k] = v


REQUIRED_FIELDS = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
OPTIONAL_FIELDS = ['cid']


def validate_passport(passport):
    present_keys = set(passport.keys())

    satisfied = REQUIRED_FIELDS.intersection(present_keys)
    if DEBUG:
        print(f"{present_keys=}{satisfied=}")
    return satisfied == REQUIRED_FIELDS


answer = 0

for pport in gen_passports(lines):
    if validate_passport(pport):
        answer += 1

print(answer)
