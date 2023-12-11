import math

inverse_connections = {'|':[(-1,0),(1,0)],
               '-':[(0,-1),(0,1)],
               'L':[(-1,0),(0,1)],
               'J':[(-1,0),(0,-1)],
               '7':[(0,-1),(1,0)],
               'F':[(1,0),(0,1)]}

connections = {(-1,0):['|','7','F'],
               (0,1):['-','J','7'],
               (1,0):['|','L','J'],
               (0,-1):['-','L','F']}

def get_cell(grid,position):
    try:
        return grid[position]
    except Exception:
        return None

def get_connected_neighbours(grid,current,ignore):
    neighbours = []
    current_pipe = get_cell(grid,current)
    if current_pipe == 'S':
        directions = connections
    else:
        directions = inverse_connections[current_pipe]
    for direction in directions:
        if direction == ignore:
            continue
        neighbour = add_tuple(direction,current)
        if get_cell(grid,neighbour) in connections[direction]:
            neighbours.append((inverse_tuple(direction),neighbour))
    return neighbours

def add_tuple(a,b):
    return (a[0]+b[0],a[1]+b[1])

def inverse_tuple(a):
    return (-a[0],-a[1])

def parse_grid(input_data):
    grid = {}
    start = None
    for y,line in enumerate(input_data):
        for x,character in enumerate(line):
            grid[(y,x)] = character
            if character == 'S':
                start = (y,x)
                pass
            pass
        pass
    return grid,start

def part1(input_data):
    grid,start = parse_grid(input_data)
    
    neighbours = get_connected_neighbours(grid,start,None)
    left = neighbours[0]
    right = neighbours[1]
    step = 0
    print(start)
    while left[1] != right[1]:
        print(f"{get_cell(grid,left[1])} {get_cell(grid,right[1])}")
        
        left = get_connected_neighbours(grid,left[1],left[0])[0]
        right = get_connected_neighbours(grid,right[1],right[0])[0]
        step += 1
    step += 1
    return step

def flood(grid,marked,path_nodes):
    to_be_added = set()
    not_started = 1
    while len(to_be_added) != 0 or not_started:
        not_started = 0
        for add in to_be_added:
            marked.add(add)
            to_be_added = set()
        for tile in marked:
            for direction in [(y, x) for y in range (-1, 2) for x in range (-1, 2)]:
                neighbour = add_tuple(direction,tile)
                if get_cell(grid,neighbour) == None:
                    continue
                if neighbour not in path_nodes:
                    if neighbour not in marked:
                        to_be_added.add(neighbour)
                        pass
                    pass
                pass
            pass
        pass
    return len(marked)

def rotate_tuple(a,angle):
    angle = math.radians(angle)
    return (a[0]*(math.sin(angle) + math.cos(angle)),a[1]*(math.cos(a)-math.sin(a)))

def part2(input_data):
    grid,start = parse_grid(input_data)
    
    marked = set()
    ######## need to be refactored
    neighbour = get_connected_neighbours(grid,start,None)[0]
    path = []
    nodes = set()
    nodes.add(start)
    while neighbour!=start:
        path.append(neighbour)
        nodes.add(neighbour[1])
        neighbour = get_connected_neighbours(grid,neighbour[1],neighbour[0])
        if len(neighbour) == 0:
            break
        neighbour = neighbour[0]
        pass
    
    for node in path:
        direction, position = node
        enclosing_direction = [-direction[1],direction[0]]
        enclosing_tile = add_tuple(position,enclosing_direction)
        if enclosing_tile not in nodes:
            marked.add(enclosing_tile)
    ######## need to be refactored
    neighbour = get_connected_neighbours(grid,start,None)[1]
    path = []
    nodes = set()
    nodes.add(start)
    while neighbour!=start:
        path.append(neighbour)
        nodes.add(neighbour[1])
        neighbour = get_connected_neighbours(grid,neighbour[1],neighbour[0])
        if len(neighbour) == 0:
            break
        neighbour = neighbour[0]
        pass
    
    for node in path:
        direction, position = node
        enclosing_direction = [direction[1],-direction[0]]
        enclosing_tile = add_tuple(position,enclosing_direction)
        if enclosing_tile not in nodes:
            marked.add(enclosing_tile)
    
    outcome = flood(grid,marked, nodes)
    
    return outcome
