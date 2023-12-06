import re,math

def calculate_distance(time_held,race_time):
    return (race_time - time_held) * time_held

def calculate_possibilities(race_time, record_distance):
    discriminant = race_time**2 - 4*record_distance
    return math.ceil((-race_time-math.sqrt(discriminant))/-2) - math.floor((-race_time+math.sqrt(discriminant))/-2) - 1

def part1(input_data):
    times = [int(t) for t in re.split(r'\s+', input_data[0])[1:]]
    distances = [int(d) for d in re.split(r'\s+', input_data[1])[1:]]
    
    prod = 1
    for i,time in enumerate(times):
        possibilities = calculate_possibilities(time,distances[i])
        print(possibilities)
        prod *= possibilities
        pass
    return prod

def part2(input_data):
    time = int("".join([t for t in input_data[0] if t.isdigit()]))
    distance = int("".join([t for t in input_data[1] if t.isdigit()]))
    
    possibilities = calculate_possibilities(time,distance)
    return possibilities
