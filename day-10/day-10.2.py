# https://adventofcode.com/2022/day/10

import os
import sys

def doday(data):
    x = 1
    cycles = []

    for line in data:
        opcode = line.split(' ')
        instr = opcode[0]
    
        if instr == 'addx':
            cycles.append(x)
            # print(f'{"".ljust(10)} CYCLE: {len(cycles):3} VAL: {cycles[len(cycles) - 1]:3} RG: {x}')
            cycles.append(x)
            x += int(opcode[1])
        elif instr == 'noop':
            cycles.append(x)
        else:
            raise ValueError(f'Unsupported instruction "{instr} {data}"')

        # print(f'{line.ljust(10)} CYCLE: {len(cycles):3} VAL: {cycles[len(cycles) - 1]:3} RG: {x}')

    print(cycles)
    for pc in range(0, 240, 40):
        for px in range(0, 40):
            sprite = cycles[pc + px]
            if px in range(sprite - 1, sprite + 2):
                print('#', end='')
            else:
                print(' ', end='')
        print()


def read_data(name):
    with open(os.path.join(os.path.dirname(sys.argv[0]), name)) as f:
        data = [ line.strip() for line in f.readlines() ]
    return data

def main():
    print('--- Sample ---')
    doday(read_data('sample-data'))
    print('--- Real ---')
    doday(read_data('data'))

if __name__ == '__main__':
    main()