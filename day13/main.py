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


def validate_winning_timestamp(timestamp, schedule):
    """Part 2"""
    offsets = [(int(bus), i) for i, bus in enumerate(schedule) if bus != 'x']

    for bus, offset in offsets:
        result = (timestamp + offset) / bus
        if result != int(result):
            return False

    return True


def find_winning_timestamp(schedule):
    """Part 2"""
    offsets = [(int(bus), i) for i, bus in enumerate(schedule) if bus != 'x']

    interval, timestamp = offsets.pop(0)

    while offsets:
        period, offset = offsets[0]
        if (timestamp + offset) % period == 0:
            interval *= period
            offsets.pop(0)
        else:
            timestamp += interval

    if validate_winning_timestamp(timestamp, schedule):
        debug(f"valid: {timestamp}")

    return timestamp


lines = [line.strip() for line in fileinput.input()]

epoch = int(lines[0])
schedule = [b for b in lines[1].split(',')]
debug(f"{epoch=}")
debug(f"{schedule=}")


# Part 1
# wait, bus = find_wait_and_bus(epoch, schedule)


answer = find_winning_timestamp(schedule)

debug('---- DEBUG ENDS ----')

print(answer)
