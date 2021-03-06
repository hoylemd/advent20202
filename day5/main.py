DEBUG = False

FILENAME = 'test.txt'
FILENAME = 'data.txt'

with open(FILENAME) as fp:
    items = [line.strip() for line in fp.readlines() if line.strip()]


class Seat:
    def __init__(self, code):
        self.code = code

        self.row = self.parse_row()
        self.column = self.parse_column()

        self.id = self.row * 8 + self.column

    def parse_row(self, code=None, min_v=0, max_v=127):
        if code is None:
            code = self.code[:7]

        if code == '':
            if min_v == max_v:
                return min_v
            else:
                raise ValueError(f"Row did not converge {min_v}, {max_v}")

        this_step = code[:1]
        rest = code[1:]
        if DEBUG:
            print(f"Parsing '{this_step}':{rest} ({min_v}, {max_v})")

        delta = int((max_v - min_v + 1) / 2)

        if this_step == 'F':
            max_v -= delta

        elif this_step == 'B':
            min_v += delta

        return self.parse_row(rest, min_v, max_v)

    def parse_column(self, code=None, min_v=0, max_v=7):
        if code is None:
            code = self.code[7:]

        if code == '':
            if min_v == max_v:
                return min_v
            else:
                raise ValueError(f"Column did not converge {min_v}, {max_v}")

        this_step = code[:1]
        rest = code[1:]
        if DEBUG:
            print(f"Parsing '{this_step}':{rest} ({min_v}, {max_v})")

        delta = int((max_v - min_v + 1) / 2)

        if this_step == 'L':
            max_v -= delta
        elif this_step == 'R':
            min_v += delta

        return self.parse_column(rest, min_v, max_v)

    def __str__(self):
        return f"{self.code}: row {self.row}, column {self.column}, seat ID {self.id}"


answer = 0
seat_ids = []

for item in items:
    if DEBUG:
        print(f"{item=}")

    seat = Seat(item)

    seat_ids.append(seat.id)

    if DEBUG:
        print(seat)

if DEBUG:
    print(sorted(seat_ids))

prev = None
for id in sorted(seat_ids):
    if prev is None:
        prev = id
        continue

    if DEBUG:
        print(f"trying {id=} {prev=}")
    if id - prev > 1:
        answer = prev + 1
        break

    prev = id

if DEBUG:
    print()

print(answer)
