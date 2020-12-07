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


def find_outers(rules, my_bag):
    """Part 1"""
    may_contain_bags = set()
    dunno_yet = set()
    nope = set()

    for colour, contents in rules.items():
        if my_bag in contents:
            may_contain_bags.add(colour)
        elif contents:
            dunno_yet.add(colour)
        else:
            nope.add(colour)

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

    return len(may_contain_bags)


def count_inners(rules, colour):
    """Part 2"""
    total_inners = 0

    contents = rules[colour]

    if DEBUG:
        print(f"Counting contents of {colour} bag:")

    for colour, n in contents.items():
        if DEBUG:
            print(f" - contains {n} {colour} bags...")
        total_inners += n
        these_inners = count_inners(rules, colour)

        if DEBUG:
            print(f" - {colour} bags contain {these_inners}")

        total_inners += n * these_inners

        if DEBUG:
            print(f" So we're up to {total_inners} now.")

    return total_inners


with open(FILENAME) as fp:
    rule_specs = [line.strip() for line in fp.readlines()]

rules = {}

for spec in rule_specs:
    if DEBUG:
        print(f"{spec=}")

    rule = Rule(spec)
    rules[rule.colour] = rule.contents

answer = count_inners(rules, 'shiny gold')
if DEBUG:
    print('---- DEBUG ENDS ----')

print(answer)
