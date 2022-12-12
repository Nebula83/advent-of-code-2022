# https://adventofcode.com/2022/day/9

import os
import sys
import time

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x},{self.y})'

    def copy(self):
        return Point(self.x, self.y)


def uniquecount(coords):
    unique_list = (list(coords))
    return len(unique_list)
 

def printpos(h, t):
    for y in reversed(range(0, 5)):
        for x in (range(0, 6)):
            char = '.'

            if h.x == x and h.y == y:   
               char = 'H'
            else:
                for p in reversed(range(0, len(t))):
                    if t[p].x == x and t[p].y == y:   
                        char = str(p + 1)

            print(char, end='')                
        print()
    print()


def printpos2(h, t):
    for y in reversed(range(0, 21)):
        for x in (range(0, 26)):
            char = '.'

            if h.x == x and h.y == y:   
               char = 'H'
            else:
                for p in reversed(range(0, len(t))):
                    if t[p].x == x and t[p].y == y:   
                        char = str(p + 1)

            print(char, end='')                
        print()
    print()



def printtail(coords):
    tails = []
    for y in range(0, 5):
        row = []
        for x in (range(0, 6)):
            row.append('.')
        tails.append(row)

    for point in coords:
        tails[point.y][point.x] = '#'
     
    for y in reversed(range(0, 5)):
        for x in (range(0, 6)):
           print(tails[y][x], end='')
        print()


def movepoint(p, dir):
    if dir == 'L':
        p.x -= 1
    elif dir == 'R':
        p.x += 1
    elif dir == 'U':
        p.y += 1
    elif dir == 'D':
        p.y -= 1

    return p


def update(h, t):
    newpoint = Point(t.x, t.y)
    xdelta = h.x - t.x
    ydelta = h.y - t.y

    if not (abs(xdelta) <=1 and abs(ydelta) <= 1):
        if t.x != h.x and t.y != h.y:
            newpoint.x += 1 if xdelta > 0 else -1 
            newpoint.y += 1 if ydelta > 0 else -1 
        else:
            if abs(xdelta) > 1:
                newpoint.x += 1 if xdelta > 0 else -1 
            if abs(ydelta) > 1:
                newpoint.y += 1 if ydelta > 0 else -1 

    return newpoint


def doday(data):
    TAIL_COUNT = 9
    start = Point(11, 5)
    h = start.copy()
    head = [h]
    tails = [[]] * TAIL_COUNT
    points = set()

    for ti in range(0, len(tails)):
        tails[ti] = []
        tails[ti].append(start.copy())


    # Calculate head
    for line in data:
        dir, _, count =  line.rpartition(' ')
        count = int(count)
        for _ in range(0, count):
            h = h.copy()
            h = movepoint(h, dir)
            head.append(h)

    # Calculate tails
    for ti in range(0, len(tails)):
        if ti == 0:
            ref = head
        else:
            ref = tails[ti - 1]

        t = tails[ti][0].copy()
        for hi in range(1, len(head)):
            t = t.copy()
            if hi > 1:
                prevh = ref[hi - 1]
            else:
                prevh = Point(11, 5)

            t = update(ref[hi], t)
            tails[ti].append(t)
            if ti == (TAIL_COUNT - 1):
                points.add((t.x, t.y))


    # print(head)
    # for tail in tails:
        # print(tail)
    # for i in range(0, len(head)):
        # printpos2(head[i], [tail[i] for tail in tails])
        # input('')

    print(f'Unique positions {uniquecount(points)}')

def read_data(name):
    with open(os.path.join(os.path.dirname(sys.argv[0]), name)) as f:
        data = [ line.strip() for line in f.readlines() ]
    return data


def main():
    print('--- Sample 1---')
    doday(read_data('sample-data'))
    print('--- Sample 2---')
    doday(read_data('sample-data-2'))
    print()
    print('--- Real ---')
    doday(read_data('data'))

if __name__ == '__main__':
    main()

