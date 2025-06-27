from aoc.base import AoCProblem
from functools import cmp_to_key

class Day05(AoCProblem):
    def parse(self, raw_input: str):
        ordering, updates = [], []
        t = raw_input.split('\n\n')
        ordering = [int(x) for line in t[0].splitlines() for x in line.split("|")]
        updates = [list(map(int, line.split(","))) for line in t[1].splitlines()]
        rules = {}
        for i in range(0, len(ordering), 2):
            rules[ordering[i]] = rules.get(ordering[i], []) + [ordering[i + 1]]
        return rules, updates

    def part1(self):
        rules, updates = self.data
        s = 0
        for update in updates:
            positions = {page: idx for idx, page in enumerate(update)}
            valid = True
            for before, afters in rules.items():
                for after in afters:
                    if before in positions and after in positions:
                        if positions[before] >= positions[after]:
                            valid = False
                            break
                if not valid:
                    break
            if valid:
                s += update[len(update)//2]
        return s

    def part2(self):
        rules, updates = self.data
        s = 0
        for update in updates:
            positions = {page: idx for idx, page in enumerate(update)}
            valid = True
            for before, afters in rules.items():
                for after in afters:
                    if before in positions and after in positions:
                        if positions[before] >= positions[after]:
                            valid = False
                            fixed = sorted(update, key=cmp_to_key(lambda x, y: -1 if y in rules.get(x, []) else 1 if x in rules.get(y, []) else 0))
                            s += fixed[len(fixed)//2]
                            break
                if not valid:
                    break
        return s