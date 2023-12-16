
reflection_table = {(1,0):(0,-1),
                    (0,1):(-1,0),
                    (-1,0):(0,1),
                    (0,-1):(1,0)}

def inverse_tuple(a):
    return (-a[0],-a[1])

def add_tuple(a,b):
    return (a[0]+b[0],a[1]+b[1])

def parse_grid(input_data):
    grid = {}
    for y,line in enumerate(input_data):
        for x,char in enumerate(line):
            grid[(x,y)] = char
            pass
        pass
    return grid, len(input_data[0]), len(input_data)

def step(state, grid, energised, cache=set()):
    if state in cache:
        return len(energised)
    cache.add(state)
    position, direction = state
    tile = grid.get(position,'#')
    if tile != '#':
        energised.add(position)
        pass
    
    while tile != '#':
        if tile == '|' and direction[1] == 0:
            step(((position[0], position[1]-1),(0,-1)),grid,energised, cache=cache)
            step(((position[0], position[1]+1),(0,1)),grid,energised,cache=cache)
            return len(energised)
        elif tile == '-' and direction[0] == 0:
            step(((position[0]-1, position[1]),(-1,0)),grid,energised, cache=cache)
            step(((position[0]+1, position[1]),(1,0)),grid,energised,cache=cache)
            return len(energised)
        elif tile == '/' or tile == '\\':
            reflected = reflection_table[direction]
            if tile == '\\':
                reflected = inverse_tuple(reflected)
                pass
            state = (add_tuple(position,reflected),reflected)
        else:
            state = (add_tuple(position,direction),direction)
            pass
        
        if state in cache:
            return len(energised)
        cache.add(state)
        position, direction = state
        tile = grid.get(position,'#')
        if tile != '#':
            energised.add(position)
            pass
        
        pass
    return len(energised)

def print_energised(energised,width,height):       
    for y in range(height):
        for x in range(width):
            if (x,y) in energised:
                print("#",end="")
            else:
                print(" ",end="")
                pass
            pass
        print("")
        pass
    pass

def part1(input_data):
    grid, width, height = parse_grid(input_data)
    state = ((0,0),(1,0))
    energised = set()
    step(state,grid, energised)
    
    print_energised(energised,width,height)
    
    return len(energised)

def part2(input_data):
    grid, width, height = parse_grid(input_data)
    
    maximum_heat = 0
    for x in range(width):
        
        maximum_heat = max(step(((x,0),(0,1)),grid, set(),cache=set()),maximum_heat)
        maximum_heat = max(step(((x,height-1),(0,-1)),grid, set(),cache=set()),maximum_heat)
    for y in range(height):
        maximum_heat = max(step(((0,y),(1,0)),grid, set(),cache=set()),maximum_heat)
        maximum_heat = max(step(((width-1,y),(-1,0)),grid, set(),cache=set()),maximum_heat)
    #print_energised(energised,width,height)
    
    return maximum_heat
