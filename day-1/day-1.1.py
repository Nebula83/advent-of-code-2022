def main():
    # get all raw lines
    with open('data', 'r') as file:
        data = file.read()
    elves = data.split('\n\n')
    
    max_calories = 0
    for elve in elves: 
        calories = sum([int(food) for food in elve.split('\n')])
        if calories > max_calories:
            max_calories = calories
    print(f'The elve carrying the most calories totals: {max_calories}')

if __name__ == '__main__':
    main()