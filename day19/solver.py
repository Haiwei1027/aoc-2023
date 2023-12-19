def check_part(flow,workflows,part):
    if flow == "A":
        return True
    elif flow == "R":
        return False
    rules = workflows[flow]
    for rule in rules:
        if ":" in rule:
            condition,result = rule.split(":")
            for i,char in enumerate("xmas"):
                condition = condition.replace(char,str(part[i])) 
            print(condition)
            if eval(condition):
                return check_part(result,workflows,part)
        else:
            return check_part(rule, workflows, part)
    pass

def part1(input_data):
    workflows = {}
    parts = set()
    separator = input_data.index("")
    workflow_data = input_data[:separator]
    parts_data = input_data[separator+1:]
    for line in workflow_data:
        name,rest = line.split("{")
        workflows[name] = rest[:-1].split(",")
    for line in parts_data:
        line = line[1:-1]
        x,m,a,s = [int(ele[2:])for ele in line.split(",")]
        parts.add((x,m,a,s))
    print(workflows)
    print(parts)
    total = 0
    for part in parts:
        if check_part("in",workflows, part):
            total += sum(part)
    return total

def union(range_a,range_b):
    if range_a == None:
        return range_b
    if range_b == None:
        return range_a
    return ((min(range_a[0][0],range_b[0][0]),max(range_a[0][1],range_b[0][1])),
            (min(range_a[1][0],range_b[0][0]),max(range_a[1][1],range_b[0][1])),
            (min(range_a[2][0],range_b[0][0]),max(range_a[2][1],range_b[0][1])),
            (min(range_a[3][0],range_b[0][0]),max(range_a[3][1],range_b[0][1])))

def check_satisfied(condition, part_range):
    
    valid = [r for r in part_range]
    invalid = [r for r in part_range]
    rating_index = -1
    rating = ''
    for i,char in enumerate("xmas"):
        if char in condition:
            rating_index = i
            rating = char
            break
        pass
    
    a,b = valid[rating_index]
    u,v = invalid[rating_index]
    print(condition,a,b)
    
    if '>' in condition:
        x,y = condition.split(">")
    elif '<' in condition:
        y,x = condition.split("<")
    if x == rating:
        #s > y
        a = max(a,int(y)+1)
        v = min(v,int(y))
    elif y == rating:
        #s < x
        b = min(b,int(x)-1)
        u = max(u,int(x))
        pass
        
    valid[rating_index] = (a,b)
    invalid[rating_index] = (u,v)
    
    return (valid[0],valid[1],valid[2],valid[3]), (invalid[0],invalid[1],invalid[2],invalid[3])

def possibilities(part_range):
    total = 1
    for part in part_range:
        a,b = part
        total *= (b-a+1)
    return total

def check_part_range(flow,workflows,part_range):
    if flow == "A":
        return possibilities(part_range)
    elif flow == "R":
        return 0
    rules = workflows[flow]
    total = 0
    for rule in rules:
        if ":" in rule:
            condition,result = rule.split(":")
            satisfied,part_range = check_satisfied(condition, part_range)
            total += check_part_range(result,workflows,satisfied)
        else:
            total += check_part_range(rule, workflows, part_range)
            pass
        pass
    return total

def part2(input_data):
    workflows = {}
    separator = input_data.index("")
    workflow_data = input_data[:separator]
    for line in workflow_data:
        name,rest = line.split("{")
        workflows[name] = rest[:-1].split(",")
    
    part_range = ((1,4000),(1,4000),(1,4000),(1,4000))
    return check_part_range("in",workflows,part_range)
