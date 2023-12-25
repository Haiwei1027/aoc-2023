import copy,pygame,time
slopes = {'>':(1,0),'v':(0,1),'<':(-1,0),'^':(0,-1)}

def parse_grid(input_data):
    grid = {}
    for y,line in enumerate(input_data):
        for x,char in enumerate(line):
            if char == '#':
                continue
            grid[(x,y)] = char
            pass
        pass
    return grid,len(input_data[0]),len(input_data)

def find_longest(grid,start,destination,check_slope=True):
    queue = []
    queue.append((0,start,set()))
    max_distance = 0
    
    path = None
    
    while len(queue) != 0:
        queue.sort(key=lambda x:-x[0])
        distance, position, previous_nodes = queue.pop(0)
        previous_nodes.add(position)
        
        if position == destination:
            if distance > max_distance:
                max_distance = distance
                path = previous_nodes
        
        for dx in range(-1,2):
            for dy in range(-1,2):
                neighbour = (position[0]+dx,position[1]+dy)
                if neighbour in previous_nodes:
                    continue
                if neighbour not in grid:
                    continue
                if dx**2+dy**2 > 1:
                    continue
                if grid[neighbour] == '.' or not check_slope:
                    queue.append((distance+1,neighbour,copy.copy(previous_nodes)))
                elif grid[neighbour] in slopes:
                    if (dx,dy) != slopes[grid[neighbour]]:
                        continue
                    queue.append((distance+1,neighbour,copy.copy(previous_nodes)))
                else:
                    print("you shouldn't be here")
                pass
            pass
        pass
    return max_distance, path

def draw_network(nodes,edges,grid,width,height):
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    for y in range(height):
        for x in range(width):
            if (x,y) in nodes:
                pygame.draw.rect(screen,pygame.Color(180,0,0,100),(x*4,y*4,4,4))
            elif (x,y) in grid:
                pygame.draw.rect(screen,pygame.Color(0,180,0,100),(x*4,y*4,4,4))
            else:
                pygame.draw.rect(screen,pygame.Color(0,0,180,100),(x*4,y*4,4,4))
            pass
        pygame.display.update()
        time.sleep(0.01)
        pass
    for edge in edges:
        start = nodes[edge[1]]
        end = nodes[edge[2]]
        pygame.draw.line(screen,pygame.Color(180,180,0),(start[0]*4,start[1]*4),(end[0]*4,end[1]*4),4)
        pygame.display.update()
        time.sleep(0.01)
    
    for i in range(100000):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
        time.sleep(0.01)
    pass
'''
def generate_network(grid,start,destination):
    queue = []
    for dx in range(-1,2):
            for dy in range(-1,2):
                neighbour = (start[0]+dx,start[1]+dy)
                if neighbour == start or start not in grid or dx**2+dy**2 > 1:
                    continue
                queue.append((1,neighbour,0))
                pass
            pass
    #distance to get there, position, previous node id 
    closed = set()
    closed.add((1,0))
    nodes = [(1,0)]
    edges = []
    
    while len(queue) != 0:
        distance,position,previous_node = queue.pop(0)
        if position in closed:
            continue
        
        if position == destination:
            edges.append((distance,previous_node, len(nodes)))
            nodes.append(position)
            continue
        
        closed.add(position)
        neighbours = set()
        for dx in range(-1,2):
            for dy in range(-1,2):
                neighbour = (position[0]+dx,position[1]+dy)
                if neighbour == position or neighbour not in grid or dx**2+dy**2 > 1:
                    continue
                neighbours.add(neighbour)
                pass
            pass
        if len(neighbours) == 2:
            for neighbour in neighbours:
                if neighbour in closed:
                    continue
                queue.append((distance+1,neighbour,previous_node))
            pass
        elif len(neighbours) > 1:
            for neighbour in neighbours:
                if neighbour in closed:
                    continue
                queue.append((1,neighbour,len(nodes)))
                pass
            edges.append((distance,previous_node, len(nodes)))
            nodes.append(position)
            pass
    
    return nodes,edges  
'''

def get_neighbours(position,grid):
    x,y = position
    return [(x+dx,y+dy) for dx in range(-1,2) for dy in range(-1,2) if dx**2+dy**2==1 and (x+dx,y+dy) in grid]

def flood(nodes, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(nodes[node] - visited)
    return visited

def flood_network(grid):
    nodes = set()
    edges = set()
    for pos in grid:
        neighbours = get_neighbours(pos,grid)
        if len(neighbours) > 2:
            nodes.add(pos)
            pass
        pass
    for node in nodes:
        neighbours = get_neighbours(pos,grid)
        for neighbour in neighbours:
            flood(nodes)
            pass
        pass
    
def ldfs(network, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in network:
        return None
    longest_path = None
    for node in network[start]:
        if node not in path:
            newpath = ldfs(network, node, end, path)
            if newpath:
                if not longest_path or len(newpath) > len(longest_path):
                    longest_path = newpath
    return longest_path

def part1(input_data):
    grid,width,height = parse_grid(input_data)
    longest,path = find_longest(grid,(1,0),(width-2,height-1))
    return longest

def part2(input_data):
    grid,width,height = parse_grid(input_data)
    nodes,edges = flood_network(grid)
    [print(i,node) for i,node in enumerate(nodes)]
    draw_network(nodes,edges,grid,width,height)
    print(edges)
    return ldfs(nodes,edges,(1,0),(width-2,height-1))
