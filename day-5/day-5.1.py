# https://adventofcode.com/2022/day/5

import os
import re
import sys

def findmarker(data):
    for index in range(0, len(data)):
        if data[index] == '\n':
            return index


def doday(data):
    markerline = findmarker(data)
    stacks = int(data[markerline - 1][-3])
    crates = []
    # Create the stacks
    for index in range(0, stacks):
        crates.append([])
        for row in reversed(range(0, markerline - 1)):
            crate = data[row][(index * 4) + 1]
            if crate != ' ':
                crates[index].append(crate)

    # Move the stacks
    move_re = re.compile(r'move (\d+) from (\d+) to (\d+)')
    for line in data[markerline + 1:]:
        counts, fromstacks, tostacks = move_re.findall(line)[0]
        count = int(counts)
        fromstack = int(fromstacks) - 1
        tostack = int(tostacks) - 1

        for pops in range(0, count):
            crates[tostack].append(crates[fromstack].pop())
    
    # Show the tops
    print(f' Top crates are: {"".join([crate[-1] for crate in crates])}')
    

def read_data(name):
    with open(os.path.join(os.path.dirname(sys.argv[0]), name)) as f:
        data = [ line for line in f.readlines() ]
    return data


def main():
    print('--- Sample ---')
    doday(read_data('sample-data'))
    print('--- Real ---')
    doday(read_data('data'))


if __name__ == '__main__':
    main()
