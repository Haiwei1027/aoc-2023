import time

def parse_grid(input_data):
    collision = {}
    grid = {}
    for y,line in enumerate(input_data):
        for x, character in enumerate(line):
            if character  != '.':
                grid[(y,x)] = character
            pass
        pass
    width = len(input_data[0])
    height = len(input_data)
    for x in range(width):
        collision[x] = set()
        for y in range(height):
            if grid.get((y,x),'.') == 'O':
                if grid.get((y-1,x),'.') == '#':
                    collision[x].add(y)
            else:
                if grid.get((y-1,x),'.') != '.':
                    collision[x].add(y)
        
    return grid,collision,width,height

def update_collision(grid,collision,source,destination,height):
    source_y,source_x = source
    destination_y, destination_x = destination
    
    collision[source_x].discard(destination_y)
    collision[source_x].add(destination_y+1)
    if source_y != destination_y:
        collision[source_x].discard(source_y+1)
    pass

def roll(grid,collision,source, height):
    source_y,source_x = source
    lower = [c for c in collision[source_x] if c <= source_y]
    destination_y = 0
    if len(lower) != 0:
        destination_y = max(lower)
        pass
    if grid.get((source_y-1,source_x),'.') != '.':
        return
    
    grid.pop(source)
    grid[(destination_y,source_x)] = 'O'
    # print(destination_y)
    update_collision(grid,collision,source,(destination_y,source_x),height)

def print_grid(grid, height, width):
    for y in range(height):
        for x in range(width):
            if (y,x) in grid:
                print(grid[(y,x)],end="")
            else:
                print("_",end="")
                pass
            pass
        print("")
        pass
    pass

def part1(input_data):
    grid, collision, width, height = parse_grid(input_data)
    # print_grid(grid, height, width)
    # print(collision)
    for x in range(width):
        for y in range(height):
            if grid.get((y,x),'.') == 'O':
                roll(grid,collision,(y,x),height)
                # print_grid(grid, height, width)
                # print(collision)
                pass
            pass
        pass
    total = 0
    for x in range(width):
        for y in range(height):
            if grid.get((y,x),'.') == 'O':
                total += height-y
                pass
            pass
        pass
    # print_grid(grid,height,width)
    return total

def hash_state(state, width, height):
    string = ""
    for y in range(height):
        for x in range(width):
            string += state.get((x,y),'.')
            pass
        string+="\n"
        pass
    return string

def slide_horizontal(state,width,height,fall_direction):
    traversal_direction = -fall_direction
    for y in range(height):
        x = 0
        if traversal_direction == -1:
            x = width - 1
        while x >= 0 and x <= width - 1:
            if state.get((x,y),'.') == 'O':
                state.pop((x,y))
                destination = x
                while state.get((destination,y),'.') == '.' and destination >= 0 and destination <= width - 1:
                    destination += fall_direction
                destination -= fall_direction
                state[(destination,y)] = 'O'
                
            x += traversal_direction
    pass

def slide_vertical(state,width,height,fall_direction):
    traversal_direction = -fall_direction
    for x in range(width):
        y = 0
        if traversal_direction == -1:
            y = height - 1
        while y >= 0 and y <= height - 1:
            if state.get((x,y),'.') == 'O':
                state.pop((x,y))
                destination = y
                while state.get((x,destination),'.') == '.' and destination >= 0 and destination <= height - 1:
                    destination += fall_direction
                destination -= fall_direction
                state[(x,destination)] = 'O'
                
            y += traversal_direction
    pass

def cycle(state,width,height):
    slide_vertical(state,width, height,-1)
    slide_horizontal(state,width, height,-1)
    slide_vertical(state,width, height, 1)
    slide_horizontal(state,width,height, 1)
    pass

def part2(input_data):
    state = {}
    for y,line in enumerate(input_data):
        for x, character in enumerate(line):
            if character  != '.':
                state[(x,y)] = character
            pass
        pass
    height = len(input_data)
    width = len(input_data[0])
    history = {}
    i = 0
    state_hash = hash_state(state,width,height)
    while state_hash not in history:
        history[state_hash] = i
        cycle(state,width,height)
        state_hash = hash_state(state,width,height)
        i+=1
    print(f"{i} same as {history[state_hash]}")
    cycle_start = i
    cycle_length = i - history[state_hash]
    rest_to_go = (1_000_000_000 - cycle_start) % cycle_length
    for _ in range(rest_to_go):
        cycle(state,width,height)
    total = 0
    for y in range(height):
        for x in range(width):
            if state.get((x,y),'.') =='O':
                total += height-y        
    
    return total
