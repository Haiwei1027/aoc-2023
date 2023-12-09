import re
from math import gcd
from functools import reduce

def parse_line(line):
    current, children= line.split(" = ")
    children = children[1:-1].split(", ")
    return current, children

def make_tree(lines):
    tree = {}
    for line in lines:
        current, children= line.split(" = ")
        children = children[1:-1].split(", ")
        tree[current] = children
    return tree

def part1(input_data):
    tree = make_tree(input_data[2:])
    instructions = input_data[0]
    instruction_index = 0
    step = 0
    current = "AAA"
    while current != "ZZZ":
        print(current)
        instruction = instructions[instruction_index]
        if instruction == 'L':
            current = tree[current][0]
        else:
            current = tree[current][1]
            pass
        step += 1
        instruction_index = (instruction_index+1)%len(instructions)
        pass
    return step

def is_goal(currents):
    for current in currents:
        if current[-1] != "Z":
            return False
    return True

def part2(input_data):
    tree = make_tree(input_data[2:])
    instructions = input_data[0]
    instruction_index = 0
    step = 0
    current = []
    founds = []
    for key in tree:
        if key[-1] == 'A':
            current.append(key)
    while not is_goal(current):
        instruction = instructions[instruction_index]
        if instruction == 'L':
            for i,node in enumerate(current):
                current[i] = tree[node][0]
        else:
            for i,node in enumerate(current):
                current[i] = tree[node][1]
            pass
        step += 1
        instruction_index = (instruction_index+1)%len(instructions)
        print(f"{current}{step}")
        for i,node in enumerate(current):
            if node[-1] == 'Z':
                founds.append((current.pop(i), step))
                print(founds)
        pass
    intervals = [found[1] for found in founds]
    return reduce(lambda x,y:(x*y)//gcd(x,y), intervals)
