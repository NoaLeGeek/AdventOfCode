from aoc.base import AoCProblem
from functools import cmp_to_key

class Day06(AoCProblem):
    def parse(self, raw_input: str):
        index = raw_input.index("^")
        grid = raw_input.splitlines()
        start = index // (len(grid[0]) + 1), index % (len(grid[0]) + 1)
        x, y = start
        visited = set()
        dx, dy = (-1, 0)
        visited.add((x, y, dx, dy))
        while 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
            nx, ny = x + dx, y + dy
            # Turn right 90 degrees
            if grid[nx][ny] == "#":
                dx, dy = dy, -dx
            else:
                x, y = nx, ny
                # Avoid infinite loops
                if (x, y, dx, dy) in visited:
                    break
                visited.add((x,y,dx,dy))
        return grid, start, visited

    def part1(self):
        visited = {(x, y) for x, y, _, _ in self.data[2]}
        self.data = self.data[0], self.data[1], visited
        return len(visited)
    
    def part2(self):
        grid, start, visited = self.data
        s = 0
        for i, j in visited:
                # Skip the starting point
                if (i, j) == start:
                    continue
                if self.is_a_loop(grid, start, (i, j)):
                    s += 1
        return s

    def is_a_loop(self, grid, start, obs):
        x, y = start
        visited = set()
        dx, dy = (-1, 0)
        visited.add((x, y, dx, dy))
        i = 0
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
            i += 1
        return False