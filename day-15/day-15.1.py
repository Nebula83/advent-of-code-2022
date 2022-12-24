# https://adventofcode.com/2022/day/15

import os
import re
import sys

class Zone:
    def __init__(self, sensor, beacon):
        self.sensor = sensor
        self.beacon = beacon
        self.distance = self._calc_distance()


    def _calc_distance(self):
        return abs(self.sensor[0] - self.beacon[0]) + abs(self.sensor[1] - self.beacon[1])


    def issensor(self, x, y):
        sx, sy = self.sensor
        return  x == sx and y == sy


    def isbeacon(self, x, y):
        sx, sy = self.beacon
        return  x == sx and y == sy


    def inrange(self, x, y):
        sx, sy = self.sensor

        dx = abs(sx - x)
        dy = abs(sy - y)

        # inrange is ceil of sum of distances
        return ((dx + dy) <= self.distance) and not self.isbeacon(x, y) and not self.issensor(x, y)

    def __repr__(self):
        data = ''
        data += f'{{sensor: {self.sensor}, '
        data += f'beacon: {self.beacon}, '
        data += f'distance: {self.distance}}}'
        return data


def parse_data(data):
    zones = []
    parse_re = re.compile(r'x=(-?\d+), y=(-?\d+)')
    for line in data:
        pair = []
        for coords in parse_re.findall(line):
            x, y = map(int, coords)
            pair.append((x, y))
        
        zones.append(Zone(pair[0], pair[1]))

    return zones

    
def get_bounds(zones):
    points = []
    dists = []
    for zone in zones:
        points.append(zone.sensor)
        points.append(zone.beacon)
        dists.append(zone.distance)

    x = [point[0] for point in points]
    y = [point[1] for point in points]

    return (min(x), max(x), min(y), max(y), max(dists))


def doday(data, row):
    zones = parse_data(data)
    minx, maxx, miny, maxy, max_dist = get_bounds(zones)
    print((minx, maxx), (miny, maxy), max_dist)

    # for row in range(row, row + 1):
    for row in range(row, row + 1):
    # for row in range(-2, 23):
        # print(f'{row:02}', end='')
        count = 0
        for col in range(minx - max_dist, maxx + max_dist):
            colval = '.'
            for zone in zones:
                if zone.issensor(col, row):
                    colval = 'S'
                    break
                elif zone.isbeacon(col, row):
                    colval = 'B'
                    break
                elif zone.inrange(col, row):
                    colval = '#'
                    count += 1
                    break
            # print(colval, end='')
        print(f'Count {count}')


def read_data(name):
    with open(os.path.join(os.path.dirname(sys.argv[0]), name)) as f:
        data = [ line.strip() for line in f.readlines() ]
    return data


def main():
    print('--- Sample ---')
    doday(read_data('sample-data'), 10)
    print('--- Real ---')
    doday(read_data('data'), 2000000)

if __name__ == '__main__':
    main()