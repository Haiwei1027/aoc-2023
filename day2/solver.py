import re

def part1(input_data):
    max = {"red":12,"green":13,"blue":14}
    sum = 0
    for i,line in enumerate(input_data):
        rest = line.split(":")[1]
        cubes = re.split(",|;", rest)
        violated = 0
        for cube in cubes:
            for color in max:
                if color in cube:
                    if max[color] < int(cube.strip().split(" ")[0]):
                        violated = 1
                        break
                    pass
                pass
            
            if violated:
                break
            pass
        if violated:
            continue
        #print(f"{i+1} okay")
        sum += i+1
        
        pass
    print(sum)
    return sum

def part2(input_data):
    sum = 0
    for i,line in enumerate(input_data):
        max = {"red":0,"green":0,"blue":0}
        rest = line.split(":")[1]
        cubes = re.split(",|;", rest)
        for cube in cubes:
            value = int(cube.strip().split(" ")[0])
            for color in max:
                if color in cube:
                    if max[color] < value:
                        max[color] = value
                        pass
                    pass
                pass
            pass
        power = max["red"]*max["green"]*max["blue"]
        sum += power
        
        pass
    return sum
