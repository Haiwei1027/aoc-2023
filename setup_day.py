from datetime import datetime
from os import mkdir, system
import requests,time

while 1:
    if (datetime.now().hour >= 5):
        break
    time.sleep(2)

DAY = datetime.now().day

template_solver = """

def part1(input_data):
    
    pass

def part2(input_data):
    
    pass
"""

system(f"start \"\" https://adventofcode.com/2023/day/{DAY}")
try:
    mkdir(f"day{DAY}")
except FileExistsError as _:
    print("Today has already been setup")
    quit()
    
with open(f"day{DAY}/solver.py","w+") as solver:
    solver.write(template_solver)
    pass
files_to_create = ["__init__.py","test1.txt","test2.txt"]
for file in files_to_create:
    with open(f"day{DAY}/{file}","w+") as created_file:
        pass

#download input
url = f"https://adventofcode.com/2023/day/{DAY}/input"
cookie = {"session":"53616c7465645f5f3f8e057c8bfa093809c8313360aa832b707df88ecd3bc8411badff7f737b84d9c17ba8cdefc1a032eb034e856d2f3839c0f0fd90e33fec8c"}
response = requests.get(url,cookies=cookie)
if response.status_code == 200:
    with open(f"day{DAY}/input.txt","w+") as puzzle_input:
        puzzle_input.write(response.text)
        pass
else:
    print("Failed to download input")