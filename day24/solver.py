import re, math
import numpy as np
from sympy import Eq,solve,symbols

MIN = 200000000000000
MAX = 400000000000000

def parse_stones(input_data,ignore_z=True):
    stones = []
    for line in input_data:
        a,b,c,x,y,z = [int(n) for n in re.findall(r'-?\d+', line)]
        
        if ignore_z:
            stone = ((a,b),(x,y))
        else:
            stone = ((a,b,c),(x,y,z))
        print(stone)
        stones.append(stone)
    return stones

def magnitude(a):
    result = 0
    for x in a:
        result += x**2
        pass
    return math.sqrt(result)

def scale(a,b):
    return (a[0]*b,a[1]*b)

def normalise(a):
    if magnitude(a) == 0:
        return a
    return scale(a,1/magnitude(a))

def dot(a,b):
    result = 0
    for x in a:
        for y in b:
            result += x*y
            pass
        pass
    return result

def collinear(a,b):
    return abs(dot(normalise(a),normalise(b))) == 1

def path_cross(stone_a,stone_b,ignore_z=True):
    intersection = None
    p1,v1 = stone_a
    p2,v2 = stone_b
    if ignore_z:
        m = np.array([[v1[0], -v2[0]],[v1[1], -v2[1]]])
        try:
            m_inv = np.linalg.inv(m)
        except Exception as e:
            return None
        result = np.dot(m_inv, np.array([p2[0]-p1[0],p2[1]-p1[1]]))
        if result[0] >= 0 and result[1] >= 0:
            return (p1[0]+result[0]*v1[0],p1[1]+result[0]*v1[1])
    else:
        
        pass
    return intersection



def part1(input_data):
    stones = parse_stones(input_data,ignore_z=True)
    count = 0
    for i,stone_a in enumerate(stones[:-1]):
        for stone_b in stones[i+1:]:
            intersection = path_cross(stone_a,stone_b)
            if intersection == None:
                continue
            if intersection[0] >= MIN and intersection[0] <= MAX:
                if intersection[1] >= MIN and intersection[1] <= MAX:
                    count += 1 
    return count

def intersects(stone_a,stone_b):
    p1,v1 = stone_a
    p2,v2 = stone_b
    dv = np.array([[v1[0],-v2[0]],[v1[1],-v2[1]],[v1[2],-v2[2]]])
    inv_dv = np.linalg.pinv(dv)
    dp = np.array([p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2]])
    result = np.dot(inv_dv,dp)
    works = True
    for r in result:
        if r < 0:
            works = False
        if not works:
            return None
    return (p1[0]+v1[0]*result[0],p1[1]+v1[1]*result[0],p1[2]+v1[2]*result[0])

def part2(input_data):
    stones = parse_stones(input_data,ignore_z=False)
    x, y, z, vx, vy, vz, t, u, v = symbols("x y z vx vy vz t u v")

    (sx1, sy1, sz1), (svx1, svy1, svz1) = stones[0]

    eq1 = Eq(x + t * vx - svx1 * t, sx1)
    eq2 = Eq(y + t * vy - svy1 * t, sy1)
    eq3 = Eq(z + t * vz - svz1 * t, sz1)

    (sx2, sy2, sz2), (svx2, svy2, svz2) = stones[1]

    eq4 = Eq(x + u * vx - svx2 * u, sx2)
    eq5 = Eq(y + u * vy - svy2 * u, sy2)
    eq6 = Eq(z + u * vz - svz2 * u, sz2)

    (sx3, sy3, sz3), (svx3, svy3, svz3) = stones[2]

    eq7 = Eq(x + v * vx - svx3 * v, sx3)
    eq8 = Eq(y + v * vy - svy3 * v, sy3)
    eq9 = Eq(z + v * vz - svz3 * v, sz3)

    solution = solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9), (x, y, z, vx, vy, vz, t, u, v))

    print(solution)
    return solution[0][0] + solution[0][1] + solution[0][2]
