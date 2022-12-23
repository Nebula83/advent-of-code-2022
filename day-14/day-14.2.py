# https://adventofcode.com/2022/day/14

import copy
import os
import sys
import time

def parse_rocks(data):
    rocks = []
    for line in data: 
        rocks.append([list(map(int, coords.split(','))) for coords in line.split(' -> ')])
    return rocks


def flatten_rocks(rocks):
    rubble = []
    for rock in rocks:
        rubble.extend(rock)
    return rubble

    
def get_bounds(rocks):
    rubble = flatten_rocks(rocks)
    x = [rock[0] for rock in rubble]
    y = [rock[1] for rock in rubble]

    return (min(x), max(x), min(y), max(y))


def create_grid(minx, maxx, miny, maxy):
    return [['.' for _ in range(minx, maxx + 1)] for _ in range(miny, maxy + 1)]


def to_xy(minx, x, y):
    return (x-minx, y)


def add_source(map, x, y):
    map[y][x] = '+'
    return (x, y)


def add_rocks(map, rocks, minx):
    for rock in rocks:
        start = rock.pop(0)
        for segment in rock:
            # Make sure the argument to r ange are sorted ascending
            if segment[0] == start[0]:
                stones = sorted([start[1], segment[1]])
                stones[1] += 1
                for y in range(*stones):
                    map[y][start[0] - minx] = '#'
            elif segment[1] == start[1]:
                stones = sorted([start[0] - minx, segment[0] - minx])
                stones[1] += 1
                for x in range(*stones):
                    map[start[1]][x] = '#'
            start = segment


def  add_floor(rockmap, maxy):
    for x in range(len(rockmap[0])):
        rockmap[maxy + 2][x] = '#'


def produce_sand(source, rockmap):
    sx, sy = source
    while True:
        down = rockmap[sy + 1][sx] == '.'
        left = rockmap[sy + 1][sx - 1]  == '.'
        right = rockmap[sy + 1][sx + 1]  == '.'

        if not down:
            if left:
                sx -= 1
            elif right:
                sx += 1
            else:
                # No ore options left, take what we got
                break
        else:
            sy += 1

    return (sx, sy)
    

def draw_map(map, y=None, slice=None):
    if slice is None:
        slice_start = 0
        slice_end = len(map)
    else:
        slice_start = max([0, (y - (slice // 2))])
        slice_end = slice

    for row in range(slice_start, slice_end):
        for col in range(len(map[row])):
            print(map[row][col], end='')
        print()
    print()
    time.sleep(.1)


def doday(data):
    rocks = parse_rocks(data)
    minx, maxx, miny, maxy = get_bounds(rocks)
    
    offset = 10000 # first multiple of ten where outcome is the same
    rockmap = create_grid(minx - offset, maxx + offset, 0, maxy + 2)
    source = add_source(rockmap, *to_xy(minx - offset, 500, 0))
    add_rocks(rockmap, rocks, minx - offset)
    add_floor(rockmap, maxy)

    step = 0
    while True:
        step += 1
        sx, sy = source
        x, y = produce_sand(source, rockmap)
        rockmap[y][x] = 'o'
        # print(f'Units {step}')
        # draw_map(rockmap, y, 30)
        # draw_map(rockmap)
        if (x == sx and y ==sy):
            print(f'Done after {step} units')
            break
    # draw_map(rockmap)


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

