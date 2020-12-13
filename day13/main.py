import fileinput

DEBUG = True


def debug(*args):
    if DEBUG:
        print(*args)


def find_wait_and_bus(epoch, schedule):
    """Part 1"""
    earliest = None
    bus_no = None
    for bus in schedule:
        if bus == 'x':
            continue

        bus = int(bus)

        dep_at = bus * (int(epoch / bus) + 1)

        if earliest is None or dep_at < earliest:
            earliest = dep_at
            bus_no = bus

    debug(f"{earliest=}, {epoch=}, {bus_no}")
    wait = earliest - epoch

    return wait, bus_no


def indexed(iterator):
    i = 0
    for item in iterator:
        yield item, i
        i += 1


def validate_winning_timestamp(timestamp, schedule):
    """Part 2"""
    offsets = {int(bus): i for bus, i in indexed(schedule) if bus != 'x'}
    earliest = 0

    debug(offsets)

    return earliest


lines = [line.strip() for line in fileinput.input()]

epoch = int(lines[0])
schedule = [b for b in lines[1].split(',')]
debug(f"{epoch=}")
debug(f"{schedule=}")

# Part 1
# wait, bus = find_wait_and_bus(epoch, schedule)

answer = validate_winning_timestamp(0, schedule)

debug('---- DEBUG ENDS ----')

print(answer)
