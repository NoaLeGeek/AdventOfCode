import sys
from importlib import import_module
from pathlib import Path

def run(year: str, day: str, mode: str = "full"):
    day_str = f"day{int(day):02d}"
    module_path = f"{year}.{day_str}.solution"
    cls_name = f"Day{int(day):02d}"

    try:
        module = import_module(module_path)
        cls = getattr(module, cls_name)
    except (ModuleNotFoundError, AttributeError):
        print(f"❌ Unable to find the module or class for {module_path}.{cls_name}")
        return

    filename = "input-full.txt" if mode == "full" else "input-test.txt"
    input_path = Path(year) / day_str / filename

    if not input_path.exists():
        print(f"❌ Input file not found: {input_path}")
        return

    solver = cls(input_path=input_path)
    solver.solve()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <year> <day> [full|test]")
        sys.exit(1)

    year = sys.argv[1]
    day = sys.argv[2]
    mode = sys.argv[3] if len(sys.argv) > 3 else "full"
    run(year, day, mode)