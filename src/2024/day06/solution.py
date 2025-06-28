from aoc.base import AoCProblem
from functools import cmp_to_key

class Day06(AoCProblem):
    def parse(self, raw_input: str):
        index = raw_input.index("^")
        lines = raw_input.splitlines()
        return lines, index // (len(lines[0])+1), index % (len(lines[0])+1)

    def part1(self):
        grid, x, y = self.data
        visited = set()
        visited.add((x, y))
        dx, dy = (-1, 0)
        while 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
            nx, ny = x + dx, y + dy
            # Turn right 90 degrees
            if grid[nx][ny] == "#":
                dx, dy = dy, -dx
            else:
                x, y = nx, ny
                visited.add((x,y))
        return len(visited)
    
    def part2(self):
        grid, x, y = self.data
        s = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "#" and grid[i][j] != "^" and self.is_a_loop(grid, (x,y), (i,j)):
                    s += 1
        return s

    def is_a_loop(self, grid, pos, obs):
        x, y = pos
        visited = set()
        dx, dy = (-1, 0)
        visited.add((x, y, dx, dy))
        while 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
            nx, ny = x + dx, y + dy
            # Turn right 90 degrees
            if grid[nx][ny] == "#" or (nx, ny) == obs:
                dx, dy = dy, -dx
            else:
                x, y = nx, ny
                if (x, y, dx, dy) in visited:
                    return True
                visited.add((x,y,dx,dy))
        return False