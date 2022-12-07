# https://adventofcode.com/2022/day/X

import os
import sys

def updir(usage, curdir):
    child =  os.path.join(*curdir)
    curdir.pop()
    parent =  os.path.join(*curdir)
    usage[parent] += usage[child]


def doday(data):
    usage = {}
    curdir = []
    for line in data:
        parts = line.split(" ")
        try:
            size = int(parts[0])
            path = os.path.join(*curdir)
            usage[path] += size
        except ValueError:
            if parts[1] == 'cd':
                dir = parts[2]
                if (dir == ".."):
                    updir(usage, curdir)
                else:
                    curdir.append(dir)
                    path = os.path.join(*curdir)
                    usage[path] = 0

    # Pop the dir until we are back at /
    while len(curdir) > 1:
        updir(usage, curdir)

    smallest = dict(filter(lambda elem: elem[1] < 100000, usage.items()))
    print(f'Sum of the smallest folders: {sum(smallest.values())}')

    all = 70000000
    used = usage["/"]
    free = all - used
    required = 30000000 - free

    print(f'Total usage: {used}, {free} free, {required} required')
    
    smallest = sorted(list(filter(lambda elem: elem >= required, usage.values())))
    print(f'Size to clean: {smallest[0]}')


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
