from typing import AnyStr


def read_input() -> AnyStr:
    with open("input-test.txt" if input() == "test" else "input-full.txt", "r") as file:
        return file.read()