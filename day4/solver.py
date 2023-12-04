

def part1(input_data):
    result = 0
    
    for line in input_data:
        numbers = line.split(":")[1].replace("  "," ").split(" ")[1:]
        separator = numbers.index("|")
        winning_numbers = set([int(n) for n in numbers[:separator]])
        my_numbers = [int(n) for n in numbers[separator+1:]]
        
        point = 0
        
        for n in my_numbers:
            if n in winning_numbers:
                if point == 0:
                    point = 1
                else:
                    point *= 2
                pass
            pass
        result += point
        pass
    return result

def part2(input_data):
    values = []
    cards = [1 for n in range(len(input_data))]
    
    for line_index, line in enumerate(input_data):
        numbers = line.split(":")[1].replace("  "," ").split(" ")[1:]
        separator = numbers.index("|")
        winning_numbers = set([int(n) for n in numbers[:separator]])
        my_numbers = [int(n) for n in numbers[separator+1:]]
        
        point = 0
        
        for n in my_numbers:
            if n in winning_numbers:
                point += 1
            pass
        values.append(point)
        for i in range(point):
            cards[line_index+i+1] += cards[line_index]
            pass
        print(point)
        print(cards)
        
        pass
    
    
    return sum(cards)
