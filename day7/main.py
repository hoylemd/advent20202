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
    rule_specs = [line.strip() for line in fp.readlines()]

answer = 0
rules = {}

may_contain_bags = set()
dunno_yet = set()
nope = set()

my_bag = 'shiny gold'

for spec in rule_specs:
    if DEBUG:
        print(f"{spec=}")

    rule = Rule(spec)
    rules[rule.colour] = rule.contents

    if my_bag in rule.contents:
        may_contain_bags.add(rule.colour)
    elif rule.contents:
        dunno_yet.add(rule.colour)
    else:
        nope.add(rule.colour)

while(dunno_yet):
    this_step = dunno_yet
    dunno_yet = set()

    for colour in this_step:
        contents = set(rules[colour].keys())
        if may_contain_bags & contents:
            may_contain_bags.add(colour)
        elif nope & contents == contents:
            nope.add(colour)
        else:
            dunno_yet.add(colour)


if DEBUG:
    print('---- DEBUG ENDS ----')

print(len(may_contain_bags))
