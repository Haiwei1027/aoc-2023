
def parse_input(input_data):
    occupied_rows = set()
    occupied_cols = set()
    galaxies = []
    for y,line in enumerate(input_data):
        for x, character in enumerate(line):
            if character == '#':
                galaxies.append((y,x))
                occupied_rows.add(y)
                occupied_cols.add(x)
                pass
            pass
        pass
    return occupied_rows,occupied_cols,galaxies

def sum_pair_distances(occupied_rows,occupied_cols,galaxies,scale):
    multiplier = scale - 1
    sum = 0
    for i,galaxy in enumerate(galaxies[:-1]):
        for j,other in enumerate(galaxies[i+1:]):
           left = min(galaxy[1],other[1])
           right = max(galaxy[1],other[1])
           xd = (right-left)+len([x for x in range(left,right) if x not in occupied_cols])*multiplier
           
           up = min(galaxy[0],other[0])
           down = max(galaxy[0],other[0])
           yd = (down-up)+len([y for y in range(up,down) if y not in occupied_rows])*multiplier
           distance = xd + yd
           sum += distance         
    return sum

def part1(input_data):
    occupied_rows, occupied_cols, galaxies = parse_input(input_data)
    return sum_pair_distances(occupied_rows,occupied_cols,galaxies,2)

def part2(input_data):
    occupied_rows, occupied_cols, galaxies = parse_input(input_data)
    return sum_pair_distances(occupied_rows,occupied_cols,galaxies,1_000_000)
