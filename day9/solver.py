
def predict_next(numbers):
    tree = [[numbers[-1]]]
    width = 1
    while tree[-1][0] != 0 or width != len(numbers)-1:
        width += 1
        tree[0].insert(0,numbers[-width])
        tree.append([])
        for i,layer in enumerate(tree[:-1]):
            tree[i+1].insert(0,layer[1]-layer[0])
    tree[-1].append(0)
    for i in range(len(tree)-2,-1,-1):
        tree[i].append(tree[i+1][-1]+tree[i][-1])
    return tree[0][-1]


def predict_before(numbers):
    tree = [[numbers[-1]]]
    width = 1
    while tree[-1][0] != 0 or width != len(numbers):
        width += 1
        tree[0].insert(0,numbers[-width])
        tree.append([])
        for i,layer in enumerate(tree[:-1]):
            tree[i+1].insert(0,layer[1]-layer[0])
    tree[-1].insert(0,0)
    for i in range(len(tree)-2,-1,-1):
        tree[i].insert(0,tree[i][0]-tree[i+1][0])
    return tree[0][0]

def part1(input_data):
    sum = 0
    for line in input_data:
        numbers = [int(n) for n in line.split(" ")]
        sum += predict_next(numbers)
    return sum

def part2(input_data):
    sum = 0
    for line in input_data:
        numbers = [int(n) for n in line.split(" ")]
        sum += predict_before(numbers)
    return sum
