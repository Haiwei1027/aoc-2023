from day17.solver import *
from solver_tester import *

from datetime import datetime
DAY = datetime.now().day

DAY = 17

full_input = []
with open(f"day{DAY}/input.txt","r") as puzzle_input:
    full_input = [line.replace("\n","") for line in puzzle_input.readlines()]

# testp1(part1,DAY)
# print(part1(full_input))

# testp2(part2,DAY)
print(part2(full_input))