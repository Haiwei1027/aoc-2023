direction_table = {"D":(0,1),"R":(1,0),"U":(0,-1),"L":(-1,0)}
convex = {"D":"R","R":"U","U":"L","L":"D"}
hex_directions = {"0":"R","1":"D","2":"L","3":"U"}

def add_tuple(a,b):
    return (a[0]+b[0],a[1]+b[1])

def multiply_tuple(a,b):
    return (a[0]*b,a[1]*b)

def part1(input_data):
    sequence = [line.split(" ") for line in input_data]
    verticies = [(0,0)]
    exterior_corners = 0
    interior_corners = 0
    perimeter = 0
    for i,command in enumerate(sequence):
        j = (i+1)%len(sequence)
        last = verticies[-1]
        direction = direction_table[command[0]]
        amount = int(command[1])
        perimeter += amount - 1
        if sequence[j][0] == convex[command[0]]:
            interior_corners += 1
        else:
            exterior_corners += 1
        next = add_tuple(last,multiply_tuple(direction,amount))
        verticies.append(next)
        pass
    #print(verticies)
    n = len(verticies)
    area = 0
    for a in range(n):
        b = (a+1)%n
        area += verticies[a][0] * verticies[b][1]
        area -= verticies[b][0] * verticies[a][1]
    area = area / 2
    area += perimeter/2
    area += (3/4)*exterior_corners+(1/4)*interior_corners
    print(perimeter)
    print(exterior_corners)
    print(interior_corners)
    return int(area)

def decode(hex):
    amount = int(hex[2:-2],16)
    direction = hex_directions[hex[-2]]
    return amount, direction

def part2(input_data):
    sequence = [line.split(" ") for line in input_data]
    for i,command in enumerate(sequence):
        hex = command[2]
        amount,direction = decode(hex)
        sequence[i] = f"{direction} {amount}"
    
    return part1(sequence)
