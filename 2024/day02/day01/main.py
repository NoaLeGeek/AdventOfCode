import os

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input-full.txt" if input() == "full" else "input-test.txt"), "r") as file:
    input = file.read()

def part1(input):
    data = [list(map(int, line.split(" "))) for line in input.split("\n")]
    safe = len(data) - [is_safe(level) for level in data].count(False)
    return safe
        

def part2(input):
    data = [list(map(int, line.split(" "))) for line in input.split("\n")]
    safe = len(data)
    for level in data:
        if is_safe(level):
            continue
        for i in range(len(level)):
            if is_safe(level[:i] + level[i+1:]):
                break
        else:
            safe -= 1
    return safe

def is_safe(level):
    condition = []
    for i in range(len(level)-1):
        distance = abs(level[i] - level[i+1])
        if distance < 1 or distance > 3:
            return False
        condition.append(level[i] < level[i+1])
        if not all(condition) and any(condition):
            return False
    return True

print(part1(input))
print(part2(input))
