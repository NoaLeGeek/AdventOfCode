from typing import AnyStr


def read_input() -> AnyStr:
    with open("input-full.txt" if input() == "full" else "input-test.txt", "r") as file:
        return file.read()


def replace_all(elements: list, old_segment: list, new_segment: list) -> list:
    if len(old_segment) > len(elements):
        return elements
    if len(old_segment) == len(elements):
        return elements if elements != old_segment else new_segment
    for i in range(len(elements) - len(old_segment) + 1):
        if elements[i:i + len(old_segment)] == old_segment:
            elements[i:i + len(old_segment)] = new_segment
    return elements
