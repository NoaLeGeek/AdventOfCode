import os

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input-full.txt" if input() == "full" else "input-test.txt"), "r") as file:
    input = file.read()

def part1(input):
    duos = [groups.split("   ") for groups in input.split("\n")]
    lists = [sorted([int(duo[i]) for duo in duos]) for i in range(2)]
    distance = [abs(lists[0][i] - lists[1][i]) for i in range(len(lists[0]))]
    return sum(distance)

def part2(input):
    duos = [groups.split("   ") for groups in input.split("\n")]
    lists = [[int(duo[i]) for duo in duos] for i in range(2)]
    score = sum([number * lists[1].count(number) for number in lists[0]])
    return score

print(part1(input))
print(part2(input))
