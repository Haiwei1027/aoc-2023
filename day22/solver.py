import re
import copy

def parse_bricks(input_data):
    bricks = []
    for line in input_data:
        a,b,c,x,y,z = [int(q) for q in re.findall(r'\d+',line)]
        start = (a,b,c)
        end = (x,y,z)
        for i in range(3):
            if end[i] < start[i]:
                start[i],end[i] = end[i],start[i]
        bricks.append((start,end))
    return bricks

def sort_bricks(bricks):
    global ids
    bricks.sort(key=lambda x:min(x[0][2],x[1][2]))
    for i,brick in enumerate(bricks):
        ids[brick] = i
    

def get_brick_tiles(brick):
    start,end = brick
    a,b,c = start
    x,y,z = end
    tiles = []
    for u in range(a,x+1):
        for v in range(b,y+1):
            for w in range(c,z+1):
                tiles.append((u,v,w))
                pass
            pass
        pass
    return tiles
    

def supports(brick_a,brick_b):
    brick_b = move_down(brick_b)
    for tile_a in get_brick_tiles(brick_a):
        for tile_b in get_brick_tiles(brick_b):
            if tile_b == tile_a:
                return True
            pass
        pass
    return False

def find_supports(brick,bricks_fell,supported_table,supporting_table):
    down_brick = move_down(brick)
    supported = False
    for tile in get_brick_tiles(down_brick):
        for support in bricks_fell:
            if tile in get_brick_tiles(support):
                supported = True
                if brick not in supported_table:
                    supported_table[brick] = set()
                supported_table[brick].add(support)
                if support not in supporting_table:
                    supporting_table[support] = set()
                supporting_table[support].add(brick)
                pass
            pass
        pass
    return supported

def move_down(brick):
    start,end = brick
    a,b,c = start
    x,y,z = end
    return ((a,b,c-1),(x,y,z-1))

def on_ground(brick):
    start,end = brick
    a,b,c = start
    return c <= 0

ids = {}

def fall_bricks(bricks):
    global ids
    bricks_fell = []
    supported_table = {}
    supporting_table = {}
    for i,brick in enumerate(bricks):
        id = ids[brick]
        if i % 50 == 0:
            print(i)
        supported = False
        while not supported:
            supported = find_supports(brick,bricks_fell,supported_table,supporting_table)
            if on_ground(brick):
                supported = True
            if not supported:
                brick = move_down(brick)
        ids[brick] = id
        bricks_fell.insert(0,brick)
        pass
    return supported_table,supporting_table,bricks_fell

def is_sole_supporter(brick,supported_table,supporting_table):
    for supported in supporting_table[brick]:
        if len(supported_table[supported]) == 1:
            return True
        pass
    return False

def part1(input_data):
    bricks = parse_bricks(input_data)
    print("parsed")
    sort_bricks(bricks)
    print("sorted")
    bricks = bricks
    supported_table,supporting_table,bricks_fell = fall_bricks(bricks)
    for key in supported_table:
        print(f"{ids[key]} {key} supported by {[(ids[x],x) for x in supported_table[key]]}")
    for key in supporting_table:
        print(f"{ids[key]} {key} supporting {[(ids[x],x) for x in supporting_table[key]]}")
    
    count = 0
    for brick in bricks_fell:
        #not supporting anything
        if brick in supporting_table:
            #supporting something thats supported by something else
            if is_sole_supporter(brick,supported_table,supporting_table):
                continue
            
            #for supported in supporting_table[brick]:
                #supported_table[supported].remove(brick)
            #pass
            #supporting_table.pop(brick)
            pass
        
        print(f"removed {ids[brick]}")
        count += 1
        pass
    
        
    return count

def disintegrate_brick(brick,supported_table,supporting_table):
    if brick in supporting_table:
        for supported in supporting_table[brick]:
            supported_table[supported].remove(brick)
            pass
    if brick in supported_table:
        supported_table.pop(brick)
    
    
def get_unstable_bricks(supported_table):
    unstables = set()
    for brick in supported_table:
        if len(supported_table[brick]) == 0:
            unstables.add(brick)
            pass
        pass
    return unstables

def collapse(brick,supported_table,supporting_table):
    if brick not in supporting_table:
        return 0
    disintegrate_brick(brick,supported_table,supporting_table)
    count = 0
    unstables = get_unstable_bricks(supported_table)
    while len(unstables) > 0:
        #delete unstable bricks
        for unstable in unstables:
            disintegrate_brick(unstable,supported_table,supporting_table)
            count += 1
        unstables = get_unstable_bricks(supported_table)
    return count
    

def part2(input_data):
    bricks = parse_bricks(input_data)
    print("parsed")
    sort_bricks(bricks)
    print("sorted")
    bricks = bricks
    supported_table,supporting_table,bricks_fell = fall_bricks(bricks)
    for key in supported_table:
        print(f"{ids[key]} {key} supported by {[(ids[x],x) for x in supported_table[key]]}")
    for key in supporting_table:
        print(f"{ids[key]} {key} supporting {[(ids[x],x) for x in supporting_table[key]]}")
    count = 0
    
    for brick in bricks_fell:
        chain = collapse(brick,copy.deepcopy(supported_table),copy.deepcopy(supporting_table))
        print(f"removed {ids[brick]} {chain}")
        count += chain
        pass
    return count