import os 
import sys

def main():
    # get all raw lines
    with open(os.path.join(os.path.dirname(sys.argv[0]), 'data'), 'r') as file:
        data = file.read()
    elves = data.split('\n\n')
    
    calories = []
    for elve in elves: 
        booba = elve.split('\n')
        calories.append(sum([int(food) for food in booba]))
    print(f'The elve carrying the most calories totals: {max(calories)}')

if __name__ == '__main__':
    main()