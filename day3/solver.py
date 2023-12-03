
def is_special(character):
    if character == '.':
        return False
    if character.isdigit():
        return False
    return True

def neighbours(line_index,character_index, height, width):
    ns = []
    for y in range(line_index-1,line_index+2):
        for x in range(character_index-1,character_index+2):
            if (y < 0 or y >= height):
                continue
            if (x < 0 or x >= width):
                continue
            ns.append((y,x)) 
            pass
        pass
    return ns
    
def fullnumber(input_data,pos):
    y,left = pos
    line = input_data[y]
    while line[left].isdigit():
        left -= 1
        if left < 0:
            break
    left += 1
    right = left
    while line[right].isdigit():
        right += 1
        if right >= len(line):
            break
    return int(line[left:right])

def part1(input_data):
    height = len(input_data)
    width = len(input_data[0])
    total = 0
    for line_index,line in enumerate(input_data):
        for character_index, character in enumerate(line):
            if is_special(character):
                digit_neighbours = [n for n in neighbours(line_index,character_index,height,width) if input_data[n[0]][n[1]].isdigit()]
                numbers = set([fullnumber(input_data,n) for n in digit_neighbours])
                total += sum(numbers)
            pass
        pass
    return total
    pass

def part2(input_data):
    height = len(input_data)
    width = len(input_data[0])
    total = 0
    for line_index,line in enumerate(input_data):
        for character_index, character in enumerate(line):
            if is_special(character):
                digit_neighbours = [n for n in neighbours(line_index,character_index,height,width) if input_data[n[0]][n[1]].isdigit()]
                numbers = set([fullnumber(input_data,n) for n in digit_neighbours])
                if character == '*':
                    if len(numbers) == 2:
                        product = 1
                        for number in numbers:
                            product *= number
                        total += product
            pass
        pass
    return total
    pass
