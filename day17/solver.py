directions = {(1,0),(0,1),(-1,0),(0,-1)}

direction_symbols = {(1,0):">",(0,1):"V",(-1,0):"<",(0,-1):"^",(0,0):"O"}

def parse_grid(input_data):
    grid = {}
    for y,line in enumerate(input_data):
        for x,char in enumerate(line):
            grid[(x,y)] = int(char)
            pass
        pass
    return grid,len(input_data[0]),len(input_data)

def add_tuple(a,b):
    return (a[0]+b[0],a[1]+b[1])

def sub_tuple(a,b):
    return (a[0]-b[0],a[1]-b[1])

def dotproduct_tuple(a,b):
    return a[0]*b[0]+a[1]*b[1]

def inverse_tuple(a):
    return (-a[0],-a[1])

def norm_tuple(a):
    x = a[0]
    y = a[1]
    if x > 0:
        x = 1
    elif x < 0:
        x = -1
    if y > 0:
        y = 1
    elif y < 0:
        y = -1
    return (x,y)

def manhatten_distance(a,b):
    return abs(b[0]-a[0]) + abs(b[1]-a[1])

def in_grid(position,width,height):
    return position[0] >= 0 and position[0] < width and position[1] >= 0 and position[1] < height

def insert(list,value,key):
    for i,e in enumerate(list):
        if key(e) > key(value):
            list.insert(i,value)
            return
    list.append(value)

def find_heatloss(start,destination,grid,width,height,minimum=1,maximum=4,result={}):
    h = lambda x : manhatten_distance(x,destination)
    queue = [(0,start,(1,0),h(start),start),(0,start,(0,1),h(start),start)]
    closed = set()
    while len(queue) != 0:
        #queue.sort(key=lambda x : x[0] + h(x[1]))
        print(queue[0],queue[-1])
        #print(f"{queue[0][0]} + {h(queue[0][1])}",end="  ")
        g,position,direction,f,previous = queue.pop(0)
        
        if (position,direction) in closed:
            continue
        if not in_grid(position,width,height):
            continue
        
        result[position] = (g,direction,previous)
        if position == destination:
            #print("")
            return result
        
        neighbour = position
        for _ in range(minimum-1):
            neighbour = add_tuple(neighbour,direction)
            if neighbour == start:
                continue
            if not in_grid(neighbour,width,height):
                break
            g += grid[neighbour]
        for _ in range(minimum,maximum):
            neighbour = add_tuple(neighbour,direction)
            if neighbour == start:
                continue
            if not in_grid(neighbour,width,height):
                break
            g += grid[neighbour]
            for turn in directions:
                if dotproduct_tuple(turn,direction) != 0:
                    continue
                insert(queue,(g,neighbour,turn,g+h(neighbour),position),lambda x:x[3])
        closed.add((position,direction))
    #print("")
    return result

def part1(input_data):
    grid,width,height = parse_grid(input_data)
    grid[(0,0)] = 0
    destination = (width-1,height-1)
    start = (0,0)
    heatloss_table = find_heatloss(start,destination,grid,width,height)
    
    
    
    return heatloss_table[destination][0]

def part2(input_data):
    grid,width,height = parse_grid(input_data)
    grid[(0,0)] = 0
    destination = (width-1,height-1)
    start = (0,0)
    heatloss_table = find_heatloss(start,destination,grid,width,height,minimum=4,maximum=11)
    
    print(heatloss_table)
    
    return heatloss_table[destination][0]
