import fileinput

DEBUG = True


def debug(*args):
    if DEBUG:
        print(*args)


def find_wait_and_bus(epoch, schedule):
    """Part 1"""
    debug(f"{epoch=}")
    debug(f"{schedule=}")

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


def validate_winning_timestamp(timestamp, schedule):
    """Part 2"""
    pass


lines = [line.strip() for line in fileinput.input()]

epoch = int(lines[0])
schedule = [b for b in lines[1].split(',')]

wait, bus = find_wait_and_bus(epoch, schedule)

answer = wait * bus

debug('---- DEBUG ENDS ----')

print(answer)
