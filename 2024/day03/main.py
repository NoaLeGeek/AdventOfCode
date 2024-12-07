import os
import re

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input-full.txt" if input() == "full" else "input-test.txt"), "r") as file:
    input = file.read()

def part1(input):
    matches = re.findall(r"(mul\(\d+,\d+\))", input)
    duos = [list(map(int, duo[4:][:-1].split(","))) for duo in matches]
    return sum([duo[0]*duo[1] for duo in duos])
        
def part2(input):
    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input)
    filtered = []
    purging = False
    for match in matches:
        if match == "do()":
            purging = False
        if match == "don't()":
            purging = True
        if not purging and match not in ["do()", "don't()"]:
            filtered.append(match)
    duos = [list(map(int, duo[4:][:-1].split(","))) for duo in filtered]
    return sum([duo[0]*duo[1] for duo in duos])

print(part1(input))
print(part2(input))
