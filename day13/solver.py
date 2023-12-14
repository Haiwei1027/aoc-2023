
def load_grid(input_data):
    grid = []
    if len(input_data) == 0:
        return None
    while input_data[0] != "":
        grid.append(input_data.pop(0))
        if len(input_data) == 0:
            return grid
        pass
    if input_data[0] == "":
        input_data.pop(0)
    return grid

def deviation(string_a, string_b):
    count = 0
    for a,b in zip(string_a,string_b):
        if a!=b:
            count +=1
            pass
        pass
    return count
        

def check_mirror(grid,fetcher,size,index,target_deviation=0):
    right = index
    left = index - 1
    total_deviation = 0
    while 0 <= left and right <= size-1:
        total_deviation += deviation(fetcher(grid,left),fetcher(grid,right))
        if total_deviation > target_deviation:
            return 0
        left -= 1
        right += 1
    if total_deviation < target_deviation:
        return 0
    return index

def check_smudged_mirror(grid,fetcher,size,index):
    return check_mirror(grid,fetcher,size,index, target_deviation=1)

def check_perfect_mirror(grid,fetcher,size,index):
    return check_mirror(grid,fetcher,size,index, target_deviation=0)

def find_reflection_base(grid,fetcher,size, checker,name="base"):
    left = 0
    mirror = 0
    while left <= size-1:
        left += 1
        while deviation(fetcher(grid,left), fetcher(grid,left - 1)) > 1:
            left += 1
        if left > size-1:
            return 0
        #print(f"{name} left stopped at {left}")
        mirror = checker(grid,fetcher,size,left)
        if mirror != 0:
            return mirror
        pass
    return mirror

def get_col(grid, index):
    try:
        col = ""
        for line in grid:
            col += line[index]
        return col
    except Exception:
        return ""
def get_row(grid, index):
    try:
        row = ""
        for character in grid[index]:
            row += character
        return row
    except Exception:
        return ""

def find_reflection_row(grid, mirror_checker):
    return 100*find_reflection_base(grid,get_row,len(grid), mirror_checker,name="row")
    
def find_reflection_col(grid, mirror_checker):
    return find_reflection_base(grid,get_col,len(grid[0]), mirror_checker,name="col")

def part1(input_data):
    grid = []
    sum = 0
    grid = load_grid(input_data)
    while grid != None:
        sum += find_reflection_col(grid, check_perfect_mirror)
        sum += find_reflection_row(grid, check_perfect_mirror)
        grid = load_grid(input_data)
    return sum

def part2(input_data):
    grid = []
    sum = 0
    grid = load_grid(input_data)
    while grid != None:
        sum += find_reflection_col(grid, check_smudged_mirror)
        sum += find_reflection_row(grid, check_smudged_mirror)
        grid = load_grid(input_data)
    return sum
