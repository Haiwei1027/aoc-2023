

def run_length_encode(line):
    character = ''
    length = 0
    encoded = []
    for i,c in enumerate(line):
        if c != character:
            if character!='':
                encoded.append((i-length,character))
                pass
            character = c
            length = i
            pass
        pass
    encoded.append((len(line)-length,character))
    return encoded

def run_length_decode(encoded):
    decoded = ""
    for ele in encoded:
        decoded += ele[1]*ele[0]
    return decoded

def run_length_print(encoded,_end="\n"):
    print(run_length_decode(encoded).replace("."," "),end=_end)

def parse_line(line):
    a,b = line.split(" ")
    springs = run_length_encode(a)
    groups = [int(digit) for digit in b.split(",")]
    return springs, groups

def unknown(springs):
    for ele in springs:
        if '?' == ele[1]:
            return True
    return False

def run_length_append(encoded,new):
    if len(encoded) == 0:
        encoded.append(new)
        return
    if encoded[-1][1] == new[1]:
        encoded[-1] = (encoded[-1][0]+new[0], new[1])
    else:
        encoded.append(new)
    return

def run_length_pop_head(encoded):
    if len(encoded) == 0:
        return '.'
    if encoded[0][0] == 1:
        return encoded.pop(0)[1]
    encoded[0] = (encoded[0][0]-1,encoded[0][1])
    return encoded[0][1]

def run_length_tail(encoded):
    tail = []
    if len(encoded) == 0:
        return tail
    if encoded[0][0] > 1:
        tail.append((encoded[0][0]-1,encoded[0][1]))
    [tail.append(ele) for ele in encoded[1:]]
    return tail

def unknown_replace(springs, replacement):
    output = []
    replaced = False
    for i,spring in enumerate(springs):
        if '?' == spring[1] and not replaced:
            run_length_append(output, (1,replacement))
            if (spring[0] > 1):
                run_length_append(output, (spring[0]-1,'?'))
                pass
            replaced = True
        else:
            run_length_append(output, spring)
    return output

def satisfy(springs, groups):
    damaged = [s for s in springs if s[1] == '#']
    if len(damaged) != len(groups):
        return 0
    for a,b in zip(damaged, groups):
        if a[0] != b:
            return 0
    #run_length_print(springs,_end=" ")
    #print(groups)
    return 1

def satisfiable(springs, groups):
    damaged = [s for s in springs if s[1] != '.']
    damaged_cursor = 0
    for require in groups:
        if damaged_cursor >= len(damaged):
            return True
        ele = damaged[damaged_cursor]
        if ele[1] == '?':
            return True
        if ele[0] > require:
           return False
        damaged_cursor += 1 
    return True

def satisfiable_1(springs, groups):
    damageds = [s for s in springs if s[1] != '.']
    group_cursor = 0
    for i,damaged in enumerate(damageds):
        if damaged[1] == '?':
            return True
        if damaged[0] > groups[group_cursor]:
            return False
        if damaged[0] < groups[group_cursor]:
            if i < len(damageds) - 1:
                if damageds[i+1][1] != '?':
                    return False
        if group_cursor != len(groups) - 1:
            group_cursor += 1
        else:
            return True
    return True

def dfs_traversal(springs, groups):
    #run_length_print(springs,_end=" ")
    #print(groups)
    if unknown(springs):
        left = unknown_replace(springs, "#")
        right = unknown_replace(springs, '.')
        sum = 0
        if satisfiable_1(left,groups):
            sum += dfs_traversal(left, groups)
        if satisfiable_1(right,groups):
            sum += dfs_traversal(right, groups)
    else:
        satisfies = satisfy(springs, groups)
        return satisfies
    return sum

def stringify(springs,groups):
    return run_length_decode(springs) + ",".join(map(str,groups))

def run_length_step(encoded, amount):
    while amount > 0:
        if len(encoded) == 0:
            return False
        head_size, head = encoded[0]
        if head == '.':
            return False
        if amount >= head_size:
            encoded.pop(0)
            amount -= head_size
        else:
            if head == '#':
                return False
            encoded[0] = (head_size - amount, head)
            amount = 0
            pass
        pass
    if len(encoded) == 0:
        return True
    if encoded[0][1] == '?':
        if encoded[0][0] > 1:
            encoded[0] = (encoded[0][0]-1,'?')
        else:
            encoded.pop(0)
    elif encoded[0][1] == '#':
        return False
    return True

def dfs_traversal_look_ahead(springs, groups, previous="", cache={}, print_cache=False):
    #run_length_print(springs,_end=" ")
    #print(groups)
    hash = stringify(springs, groups)
    if hash in cache:
        return cache[hash]
    damaged_empty = len([spring for spring in springs if spring[1] == '#']) == 0
    unknown_empty = len([spring for spring in springs if spring[1] == '?']) == 0
    if len(groups) == 0:
        if damaged_empty:
            print(previous+run_length_decode(springs))
            return 1
        else:
            #print("return bad")
            return 0
    elif damaged_empty and unknown_empty:
        #print("return bad")
        return 0
        
    if springs[0][1] == '.':
            springs = springs[1:]
            pass
        
    head_size,head = springs[0]
    satisfies = 0
    if head != '#':
        previous_a = previous+'.'
        satisfies += dfs_traversal_look_ahead(run_length_tail(springs), groups,previous=previous_a,cache=cache)
    if run_length_step(springs, groups[0]):
        #print(f"write {groups[0]}")
        previous_b = previous + groups[0]*'#'+'.'
        satisfies += dfs_traversal_look_ahead(springs,groups[1:], previous=previous_b, cache=cache)
    cache[hash] = satisfies
    if print_cache:
        print(cache)
    return satisfies

def part1(input_data):
    sum = 0
    for i,line in enumerate(input_data):
        #print(f"processing line {i}")
        springs, groups = parse_line(line)
        outcome = dfs_traversal(springs, groups)
        print(outcome)
        sum += outcome
    return sum

def unfold(line):
    a,b = line.split(" ")
    return ((a+'?')*5)[:-1] + ' ' + ((b+',')*5)[:-1]

def part2(input_data):
    sum = 0
    for i,line in enumerate(input_data):
        print(f"processing line {i}")
        line = unfold(line)
        springs, groups = parse_line(line)
        print(groups)
        outcome = dfs_traversal_look_ahead(springs, groups,print_cache=False)
        print(outcome)
        sum += outcome
    return sum