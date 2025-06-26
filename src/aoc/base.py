from abc import ABC, abstractmethod
from pathlib import Path

class AoCProblem(ABC):
    def __init__(self, input_path=None):
        self.input_path = input_path or "input.txt"
        self.raw_input = self._read_input()
        self.data = self.parse(self.raw_input)

    def _read_input(self):
        path = Path(self.input_path)
        if not path.exists():
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        return path.read_text().strip()

    @abstractmethod
    def parse(self, raw_input: str):
        """Transform raw input into structured data."""
        pass

    @abstractmethod
    def part1(self) -> any:
        pass

    @abstractmethod
    def part2(self) -> any:
        pass

    def solve(self):
        print("Part 1:", self.part1())
        print("Part 2:", self.part2())