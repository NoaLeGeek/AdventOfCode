from aoc.base import AoCProblem

class Day02(AoCProblem):
    def parse(self, raw_input: str):
        t = []
        for line in raw_input.splitlines():
            t.append(list(map(int, line.split())))
        return t

    def is_valid(self, row):
        if sorted(row) not in (row, row[::-1]):
            return False
        for i in range(len(row) - 1):
            if not (0 < abs(row[i] - row[i + 1]) < 4):
                return False
        return True 

    def part1(self):
        c = 0
        for row in self.data:
            if self.is_valid(row):
                c += 1
        return c

    def part2(self):
        c = 0
        for row in self.data:
            if self.is_valid(row):
                c += 1
            else:
                for i in range(len(row)):
                    if self.is_valid(row[:i] + row[i + 1:]):
                        c += 1
                        break
        return c