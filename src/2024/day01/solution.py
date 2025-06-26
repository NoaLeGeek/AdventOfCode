from aoc.base import AoCProblem

class Day01(AoCProblem):
    def parse(self, raw_input: str):
        t = [[], []]
        for line in raw_input.splitlines():
            a, b = line.split()
            t[0].append(a)
            t[1].append(b)
        return t

    def part1(self):
        t = [sorted(self.data[0]), sorted(self.data[1])]
        s = 0
        for i in range(len(t[0])):
            s += abs(int(t[0][i]) - int(t[1][i]))
        return s

    def part2(self):
        s = 0
        for i in range(len(self.data[0])):
            element = self.data[0][i]
            s += int(element) * self.data[1].count(element)
        return s