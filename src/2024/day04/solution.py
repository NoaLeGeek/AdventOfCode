from aoc.base import AoCProblem

class Day04(AoCProblem):
    def parse(self, raw_input: str):
        return raw_input.splitlines()

    def part1(self):
        word = "XMAS"
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        count = 0
        rows, cols = len(self.data), len(self.data[0])
        for r in range(rows):
            for c in range(cols):
                for dx, dy in directions:
                    i, j = r, c
                    l = 0
                    while 0 <= i < rows and 0 <= j < cols and l < len(word):
                        if self.data[i][j] == word[l]:
                            l += 1
                        else:
                            break
                        i += dx
                        j += dy
                    if l == len(word):
                        count += 1
        return count

    def part2(self):
        word = "MAS"
        count = 0
        rows, cols = len(self.data), len(self.data[0])
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if self.data[r][c] != word[1]:
                    continue
                down_right = self.data[r-1][c-1] + self.data[r][c] + self.data[r+1][c+1]
                down_left = self.data[r-1][c+1] + self.data[r][c] + self.data[r+1][c-1]
                if (down_right in [word, word[::-1]]) and (down_left in [word, word[::-1]]):
                    count += 1
        return count