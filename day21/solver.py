
DEAD = 0
ALIVE = 1

def parse_grid(input_data):
    grid = {}
    start = (0,0)
    for y,line in enumerate(input_data):
        for x, char in enumerate(line):
            grid[(x,y)] = char
            if char == 'S':
                start = (x,y)
                pass
            pass
        pass
    return grid,start,len(input_data[0]),len(input_data)

def add_tuple(a,b):
    return (a[0]+b[0],a[1]+b[1])

def neighbours(position,grid,width,height):
    neighbours = set()
    for cell in [(0,1),(1,0),(-1,0),(0,-1)]:
        neighbour = add_tuple(cell,position)
        if get_infinite_cell(neighbour,grid,width,height) != '#':
            neighbours.add(neighbour)
    return neighbours

def get_infinite_cell(position,grid,width,height):
    x,y = position
    return grid[(x%width,y%height)]

def bfs(grid,start,step_count,width,height):
    queue = []
    closed = set()
    
    queue.append((start,0))
    
    
    while len(queue) != 0:
        position,step = queue.pop(0)
        #print_grid(input_data,[x[0] for x in queue])
        print(step)
        if step >= step_count:
            queue.append((position,step))
            return len(queue)
            #return [q[0] for q in queue]
        
        for neighbour in neighbours(position,grid,width,height):
            if neighbour in [q[0] for q in queue]:
                continue
            queue.append((neighbour,step+1))
            pass
        closed.add(position)

def count_alive(domain,width,height):
    #count = 0
    count = {}
    for pos in domain:
        grid = (pos[0]//width,pos[1]//height)
        if grid not in count:
            count[grid] = 0
        if domain[pos] == ALIVE:
            count[grid] += 1
    return count

def count_alive_total(domain,width,height):
    count = 0
    for pos in domain:
        grid = (pos[0]//width,pos[1]//height)
        if domain[pos] == ALIVE:
            count += 1
    return count

def process_cell(x,y,domain,next,grid_data,width,height):
    if domain.get((x,y),DEAD) == ALIVE:
        next[(x,y)] = DEAD
    else:
        for neighbour in neighbours((x,y),grid_data,width,height):
            if domain.get(neighbour,DEAD) == ALIVE:
                next[(x,y)] = ALIVE
                break
            pass
        pass

def flood_filter(grid,start,step_count,width,height):
    queue = []
    closed = set()
    
    queue.append((start,0))
    
    while len(queue) != 0:
        position,step = queue.pop(0)
        #print_grid(input_data,[x[0] for x in queue])
        print(step)
        if position in closed:
            continue
        if step > step_count:
            break
        
        for neighbour in neighbours(position,grid,width,height):
            if neighbour in [q[0] for q in queue]:
                continue
            queue.append((neighbour,step+1))
            pass
        closed.add(position)   
        pass
    
    filtered = set()
    for position in closed:
        x,y = position
        #print(f"{position} {x%width} + {y%height} * width = {x%width+(y%height)*width}")
        if (x%width+(y%height)*width) % 2 == 0: #fucking brakctsrdbe
            filtered.add((x,y))
            pass
        pass
    #print_grid(input_data,closed)
    #print_grid(input_data,filtered)
    return len(filtered)

def filter_entire_grid(grid,width,height,odd=True):
    count = 0
    for x in range(width):
        for y in range(height):
            if grid[(x,y)] == '#':
                continue
            #print(f"{position} {x%width} + {y%height} * width = {x%width+(y%height)*width}")
            if (x+(y)*width) % 2 == 0:
                if not odd:
                    count += 1
            else:
                if odd:
                    count += 1
        pass
    return count

def print_grid(input_data, visited):
    for y,line in enumerate(input_data):
        for x, char in enumerate(line):
            if (x,y) in visited:
                print("O",end="")
            else:
                print(char,end="")
                pass
        pass
        print("")
        pass
    pass



def part1(input_data):
    grid,start,width,height = parse_grid(input_data)
    return cellular_automata(grid,start,65+131+131,width,height)
    #print_grid( input_data, bfs(grid,start,1))

def cellular_automata(grid_data,start,step_count,width,height):
    grids = set()
    domain = {}
    next = {}
    
    grids.add((0,0))
    domain[start] = ALIVE
    print("hi")
    for i in range(step_count):
        #if i % 131 == 0:
            #print(f"{count_alive_total(domain,width,height)},")
        for grid in grids:
            grid_x, grid_y = grid
            for x in range(grid_x*width-1,(grid_x+1)*width+1):
                for y in range(grid_y*height-1,(grid_y+1)*width+1):
                    if get_infinite_cell((x,y),grid_data,width,height) == '#':
                        continue
                    process_cell(x,y,domain,next,grid_data,width,height)
                    pass
                pass
            pass
        for pos in next:
            domain[pos] = next[pos]
            x,y = pos
            grids.add((x//width,y//height))
        pass
    return count_alive(domain,width,height)

def part2(input_data):
    grid,start,width,height = parse_grid(input_data)
    half_width = width // 2
    print(start[0]+start[1]*width)
    print(width,height)
    filled_quartile_width = (26501365 - half_width) // width - 1
    print(filled_quartile_width)
    grids_even = (filled_quartile_width+1)**2
    grids_odd = (filled_quartile_width)**2
    print(f"number of even filled {grids_even} number of odd filled {grids_odd}")
    useful_data = cellular_automata(grid,start,half_width+width*2,width,height)
    
    odd_filled = useful_data[(0,0)]
    even_filled = useful_data[(-1,0)]
    print(f"odd filled {odd_filled} even filled {even_filled}")
    
    print(useful_data)
    
    north_east_triangle = useful_data[(2,-1)]
    north_east_inverse = useful_data[(1,-1)]
    
    south_east_triangle = useful_data[(2,1)]
    south_east_inverse = useful_data[(1,1)]
    
    north_west_triangle = useful_data[(-2,-1)]
    north_west_inverse = useful_data[(-1,-1)]
    
    south_west_triangle = useful_data[(-2,1)]
    south_west_inverse = useful_data[(-1,1)]
    
    north_cap = useful_data[(0,-2)]
    east_cap = useful_data[(2,0)]
    south_cap = useful_data[(0,2)]
    west_cap = useful_data[(-2,0)]
    
    solution = grids_even * even_filled + grids_odd * odd_filled
    solution += filled_quartile_width * (north_east_triangle + north_east_inverse) + north_east_triangle
    solution += filled_quartile_width * (south_east_triangle + south_east_inverse) + south_east_triangle
    solution += filled_quartile_width * (south_west_triangle + south_west_inverse) + south_west_triangle
    solution += filled_quartile_width * (north_west_triangle + north_west_inverse) + north_west_triangle
    solution += north_cap + south_cap + west_cap + east_cap
    
    return solution