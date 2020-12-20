import fileinput

DEBUG = False


def debug(*args):
    if DEBUG:
        print(*args)


def parse_instruction(line):
    """Parse the instruction line into target address and the value"""
    parts = line.split('] = ', 1)
    val = int(parts[-1])
    location = int(parts[0][4:])

    return location, val


def pad_bin_num(num, width):
    binny = f"{num:b}"
    padding = width - len(binny)

    return f"{'0' * padding}{binny}"


def print_bin_num(num, width):
    return f"{pad_bin_num(num, width)} = {num}"


def apply_mask(mask, value):
    """Part 1"""
    debug(f"applying mask to {value}")
    width = len(mask)
    t_mask = int(mask.replace('X', '0'), 2)
    f_mask = int(mask.replace('X', '1'), 2)

    debug(mask)
    debug(print_bin_num(value, width))
    debug(print_bin_num(t_mask, width))
    debug(print_bin_num(f_mask, width))

    value = value | t_mask
    value = value & f_mask

    debug(print_bin_num(value, width))

    return value


class Mask:
    def __init__(self, src):
        self.src = src
        self.width = len(src)

    def decode_address(self, addr):
        """Decode a source address into a list of addresses.

        :param int addr: The source address in integer form.
        :returns [int]: The list of masked addresses in integer form.
        """
        addr_strs = [pad_bin_num(addr, self.width)]
        for i, bit in enumerate(self.src):
            new_strs = []
            if bit == '0':
                pass
            elif bit == '1':
                new_strs = [
                    f"{addr_str[:i]}1{addr_str[i+1:]}"
                    for addr_str in addr_strs
                ]
            elif bit == 'X':
                for addr_str in addr_strs:
                    new_strs += [
                        f"{addr_str[:i]}1{addr_str[i+1:]}",
                        f"{addr_str[:i]}0{addr_str[i+1:]}"
                    ]
            else:
                raise ValueError(f"{bit=} wat")

            if new_strs:
                addr_strs = new_strs

        return [int(addr_str, 2) for addr_str in addr_strs]


lines = [line.strip() for line in fileinput.input()]

answer = 0
memory = {}

for line in lines:
    if line.startswith('mask'):
        mask = Mask(line.split(' ')[-1])
        continue

    loc, v = parse_instruction(line)

    addrs = mask.decode_address(int(loc))

    for addr in addrs:
        memory[addr] = v
        # masked = apply_mask(mask, v)
        debug(f"apply to location {addr}: {v}")

answer = sum(memory.values())

debug('---- DEBUG ENDS ----')

print(answer)
