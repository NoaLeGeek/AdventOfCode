from aoc.base import AoCProblem

class Day01(AoCProblem):
    def parse(self, raw_input: str):
        l = [[], []]
        for line in raw_input.splitlines():
            a, b = line.split()
            l[0].append(a)
            l[1].append(b)
        return l

    def part1(self):
        l = [sorted(self.data[0]), sorted(self.data[1])]
        s = 0
        for i in range(len(l[0])):
            s += abs(int(l[0][i]) - int(l[1][i]))
        return s

    def part2(self):
        s = 0
        for i in range(len(self.data[0])):
            element = self.data[0][i]
            s += int(element) * self.data[1].count(element)
        return s