DEBUG = True

FILENAME = 'test.txt'
# FILENAME = 'data.txt'


def parse_content_spec(spec):
    deets = spec.split(' bag')[0]

    parts = deets.split(' ', 1)
    colour = parts[1]
    number = int(parts[0])

    return colour, number


class Rule:
    def __init__(self, src):
        self.src = src

        self.contents = {}

        # [:-1] strips the trailing .
        parts = src[:-1].split(' bags contain ')
        self.colour = parts[0]

        if parts[1] == 'no other bags':
            return

        for spec in parts[1].split(', '):
            c, n = parse_content_spec(spec)
            self.contents[c] = n

    def __str__(self):
        return f"{self.colour}: {self.contents}"


with open(FILENAME) as fp:
    rules = [line.strip() for line in fp.readlines()]

answer = 0

for spec in rules:
    if DEBUG:
        print(f"{spec=}")

    rule = Rule(spec)
    print(rule)

if DEBUG:
    print('---- DEBUG ENDS ----')

print(answer)
