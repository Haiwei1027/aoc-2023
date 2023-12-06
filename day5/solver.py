import random,math,decimal

def get_maps(input_data):
    maps = {}
    map_index = ""
    for line in input_data:
        if ':' in line:
            map_index = line
            maps[map_index] = []
        else:
            destination_start,source_start,range_size = [int(v) for v in line.split(" ")]
            maps[map_index].append((destination_start-source_start,source_start,source_start+range_size))
    return maps

def apply_maps(seed,maps):
    for map_index in maps:
        transforms = maps[map_index]
        for transform in transforms:
            delta,start,end = transform
            if start <= seed < end:
                seed += delta
                break
    return seed

def part1(input_data):
    seeds = [int(s) for s in input_data[0].split(":")[1].split() if s.isdigit()]
    maps = get_maps(input_data[1:])
    locations = [apply_maps(seed,maps) for seed in seeds]
    print(locations)
    return min(locations)

def fromRange(seed_range):
    return seed_range[0],seed_range[0] + seed_range[1]

def anneal(seed_range,maps):
    start, end = fromRange(seed_range)
    temp = random.randint(10000,10000000)
    cooldown_rate = random.randint(800,950)/1000
    final_temp = 4
    solution = random.randint(start,end-1)
    solution_location = apply_maps(solution,maps)
    neighbor_size = random.randint(1,100)
    while temp > final_temp:
        neighbor = random.randint(max(start,solution-neighbor_size),min(end-1,solution+neighbor_size))
        neighbor_location = apply_maps(neighbor,maps)
        cost = solution_location - neighbor_location
        if cost > 0:
            solution = neighbor
            solution_location = neighbor_location
        elif random.uniform(0, 1) < decimal.Decimal((-1*(cost))/temp).exp():
            solution = neighbor
            solution_location = neighbor_location
        temp *= cooldown_rate
    return solution_location,solution

def hill_decent(seed,maps,value):
    print(f"hill {seed} {value}")
    while 1:
        changed = False
        neighbours = [seed-10,seed+10,seed-1,seed+1]
        for neighbour in neighbours:
            neighbour_value = apply_maps(neighbour,maps)
            if neighbour_value < value:
                seed = neighbour
                value = neighbour_value
                print(f"{value} from {seed}")
                changed = True
                break
            pass
        if not changed:
            return value
        pass
    pass

def part2(input_data):
    seed_input = [int(s) for s in input_data[0].split(":")[1].split() if s.isdigit()]
    seed_ranges = [(seed_input[i],seed_input[i+1]) for i in range(0,len(seed_input),2)]
    maps = get_maps(input_data[1:])
    
    #visualise_maps(maps)
    
    min_location = 999999999999
    min_range = None
    min_seed = 9999999999999999
    for seed_range in seed_ranges:
        for i in range(200):
            annealed_location,annealed_seed = anneal(seed_range,maps)
            #print(f"{annealed_location}, {annealed_seed} from {seed_range}")
            if annealed_location < min_location:
                min_seed = annealed_seed
                min_location = annealed_location
                min_range = seed_range
    print(f"{min_seed} from {min_range}")
    return hill_decent(min_seed,maps,min_location)