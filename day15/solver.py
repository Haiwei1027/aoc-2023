

def hash(string):
    hash = 0
    for character in string:
        hash += ord(character)
        hash *= 17
        hash %= 256
    return hash

def part1(input_data):
    total = 0
    sequences = input_data[0].split(",")
    for sequence in sequences:
        total += hash(sequence)
    return total

def part2(input_data):
    total = 0
    boxes = {}
    labels = {}
    sequences = input_data[0].split(",")
    for sequence in sequences:
        if '=' in sequence:
            label,focal_length = sequence.split("=")
            box = hash(label)
            if box not in boxes:
                boxes[box] = []
            if label not in boxes[box]:
                boxes[box].append(label)
            labels[label] = int(focal_length)
        elif '-' in sequence:
            label = sequence[:-1]
            box = hash(label)
            if box in boxes:
                if label in boxes[box]:
                    boxes[box].remove(label)
            pass
        pass
    print(boxes)
    for i in range(256):
        if len(boxes.get(i,[])) != 0:
            
            for j,_len in enumerate(boxes[i]):
                power = i+1
                power *= (j+1)*labels[_len]
                print(f"({i+1} * {j+1} * ({labels[_len]}))")
                total += power
    return total
