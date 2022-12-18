# https://adventofcode.com/2022/day/12

from math import hypot

import os
import sys

DEBUG=True
# DEBUG=False

def char_to_score(char):
    char_val = ord(char) - ord('A') # ascii - A
    score = 1
    if char_val > 25:
        char_val -= 32
    else:
        score += 26
    score += char_val

    return score


def check(map, pointx, pointy, current):
    isoption = False
    value = 10000

    if DEBUG: print(f'  Checking {(pointx, pointy)}: ', end='')
    if (pointx >= 0 and pointx < len(map[0])) and (pointy >= 0 and pointy < len(map)):
        value = map[pointy][pointx]
        if DEBUG: print(f'{value} yes')
    else:
        if DEBUG: print('no')
        # point does not exist
        pass


    if value == current or value == (current - 1):
        isoption = True

    return (isoption, value)


def by_height(option):
    point, value = option
    return value


def search(startx, starty, coords, map, x, y):
    current = map[y][x]
    if DEBUG: print(f'Next move for ({x}, {y}) {current}')

    # left, top, right, bottom
    options = set()
    points = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
    for point in points:
        isoption, value = check(map, *point, current)
        if isoption:
            options.add(point)
    
    # remove visited
    options = options - coords

    # Take the optimal option in the order: shortest vector, lowest number
    if DEBUG: print('Calculating closest point')
    vector = 100000 # random large number
    selection = None

    # opti = False
    opti = True
    if opti:
        for option in options:
            x, y = option
            value = map[y][x]
            deltax = x - startx
            deltay = y - starty
            h = hypot(deltax, deltay)

            print(f'  {option} V: {value} H: {h}')
            if h < vector:
                vector = h
                selection = option
    else:
        try:
            selection = options.pop()
        except:
            pass
    
    if selection:
        if DEBUG: print(f'Selected {selection} ', end='')
        x, y = selection
        value = map[y][x]
        if DEBUG: print(f'{value}')

    return selection


def doday(data):
    # Build map
    map = []
    for line in data:
        row = [char_to_score(char) for char in line]
        map.append(row)

    # Find start and end points
    start = ()
    end = ()
    for row in range(len(map)):
        for col in range(len(map[row])):
            value = map[row][col]
            if value == char_to_score('S'):
                start = (col, row)
                map[row][col] = 0
            elif value == char_to_score('E'):
                end = (col, row)
                map[row][col] = 27

    print(f'Found start point at {start} and goal at {end}')

    # start at the end and work our way back
    visited = set()
    path = []
    curpos = end
    while curpos != start:
        if DEBUG: print(f'Move: {len(path)}')
        for row in range(len(map)):
            for col in range(len(map[row])):
                value = map[row][col]
                if value == char_to_score('S'):
                    start = (col, row)
                elif value == char_to_score('E'):
                    end = (col, row)

                if (col, row) in path:
                    if DEBUG: print(f' X ', end='')
                else:
                    if DEBUG: print(f'{value:02} ', end='')
            if DEBUG: print()

        curpos = search(*start, visited, map, *curpos)
        if curpos is None: 
            if DEBUG: print('  no dice')
            # Take one step back
            path.pop()
            curpos = path[-1]
            if DEBUG: print(f'Resetted curpos to {curpos}')
        else:
            visited.add(curpos)
            path.append(curpos)

        if DEBUG: print(f'{path} : {len(path)}')
        # if DEBUG: input()
        if DEBUG: print()

    print(f'Finished in {len(path)} moves!')
    for row in range(len(map)):
        for col in range(len(map[row])):
            value = map[row][col]
            if value == char_to_score('S'):
                start = (col, row)
            elif value == char_to_score('E'):
                end = (col, row)

            if (col, row) in path:
                print(f' X ', end='')
            else:
                print(f'{value:02} ', end='')
        print()
        

def read_data(name):
    with open(os.path.join(os.path.dirname(sys.argv[0]), name)) as f:
        data = [ line.strip() for line in f.readlines() ]
    return data


def main():
    print('--- Sample ---')
    doday(read_data('sample-data'))
    # print('--- Real ---')
    # doday(read_data('data'))


if __name__ == '__main__':
    main()