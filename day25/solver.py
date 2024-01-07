import threading
import random

def parse_input(input_data):
    nodes = set()
    edges = set()
    for line in input_data:
        label,rest = line.split(":")
        rest = [r for r in rest.split(" ") if r != '']
        nodes.add(label)
        for r in rest:
            nodes.add(r)
            edges.add((label,r))
    return nodes,edges

def is_group(group,edges):
    count = 0
    for g in group:
        for edge in edges:
            a,b = edge
            if g == a:
                if b not in group:
                    count += 1  
            elif g == b:
                if a not in group:
                    count += 1
    return count <= 3

def get_neighbours(group,edges):
    neighbours = set()
    for node in group:
        for edge in edges:
            a,b = edge
            if node == a:
                if b not in group:
                    neighbours.add(b)
            elif node == b:
                if a not in group:
                    neighbours.add(a)
                    pass
                pass
            pass
        pass
    return neighbours

def hash_group(group):
    string = ""
    for node in group:
        string+=node
    return string

def group_size(group,nodes,edges):
    queue = []
    queue.append(group)
    closed = set()
    while len(queue) != 0:
        group = queue.pop(0)
        #print(group)
        if hash_group(group) in closed:
            continue
        if is_group(group,edges):
            gs = len(group)
            print(gs * (len(nodes)-gs))
            return len(group)
        new_group = group.copy()
        for neighbour in get_neighbours(group,edges):
            
            new_group.add(neighbour)
        queue.append(new_group)
        closed.add(hash_group(group))
    
    print("couldnt find")
    return None

def part1(input_data):
    nodes,edges = parse_input(input_data)
    for node in nodes:
        threading.Thread(target=group_size,args=(set([node]),nodes,edges)).start()
        pass
    return None 

def part2(input_data):
    
    pass
