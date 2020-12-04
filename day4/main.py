import re

DEBUG = False

FILENAME = 'data.txt'
if DEBUG:
    FILENAME = 'test.txt'

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

    yield pport


def is_between(value, at_least, at_most):
    parsed = int(value)
    if parsed < at_least:
        return False

    if parsed > at_most:
        return False

    return True


def year_validator(at_least, at_most):
    def valid8r(value):
        if re.match(r'[0-9]{4}', value):
            return is_between(value, at_least, at_most)

        return False

    return valid8r


def height_validator(value):
    magnitude = value[:-2]
    unit = value[-2:]

    if unit == 'cm':
        return is_between(magnitude, 150, 193)
    if unit == 'in':
        return is_between(magnitude, 59, 76)

    return False


def hair_validator(value):
    return re.match(r'#[0-9a-f]{6}', value)


def eye_validator(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def pid_validator(value):
    return re.match(r'[0-9]{9}', value)


VALID8RS = {
    'byr': year_validator(1920, 2002),
    'iyr': year_validator(2010, 2020),
    'eyr': year_validator(2020, 2030),
    'hgt': height_validator,
    'hcl': hair_validator,
    'ecl': eye_validator,
    'pid': pid_validator,
}

REQUIRED_FIELDS = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
OPTIONAL_FIELDS = ['cid']


def validate_passport(passport):
    present_keys = set(passport.keys())

    satisfied = REQUIRED_FIELDS.intersection(present_keys)

    if satisfied != REQUIRED_FIELDS:
        if DEBUG:
            print(f"Missing required fields: {REQUIRED_FIELDS.difference(satisfied)}")
        return False

    for key, value in passport.items():
        validator = VALID8RS.get(key)
        if validator is None or validator(value):
            continue

        if DEBUG:
            print(f"{key}:{value} invalid")

        return False

    return True


answer = 0
n = 0

for pport in gen_passports(lines):
    n += 1
    if validate_passport(pport):
        answer += 1
    else:
        if DEBUG:
            print(f"#{n} invalid: {pport}")

if DEBUG:
    print(f"{answer} of {n} are valid.")
else:
    print(answer)
