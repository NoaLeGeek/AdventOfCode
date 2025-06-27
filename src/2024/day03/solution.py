from aoc.base import AoCProblem
from re import findall, compile

class Day03(AoCProblem):
    def parse(self, raw_input: str):
        return raw_input

    def part1(self):
        matches = findall(r"mul\((\d+),(\d+)\)", self.data)
        s = 0
        for a, b in matches:
            s += int(a) * int(b)
        return s

    def part2(self):
        pattern = compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")
        s = 0
        purging = False
        for m in pattern.finditer(self.data):
            # Numbers
            if m.group(1) is not None and m.group(2) is not None and not purging:
                a, b = m.groups()
                s += int(a) * int(b)
            elif m.group(0) == "do()":
                purging = False
            elif m.group(0) == "don't()":
                purging = True
        return s