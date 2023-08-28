from copy import copy

import Utils
import re


def main():
    data = Utils.read_input()
    crates, moves = map(lambda x: list(str.splitlines(x)), data.split("\n\n"))
    columns_length = int(crates[-1][-1])
    crates = list(map(lambda x: Utils.replace_all(x.split(" "), ['', '', '', ''], ['']), crates[:-1]))
    columns = [[crate[i] for crate in crates if i < len(crate) and crate[i] != ''] for i in range(columns_length)]
    print(len(columns))
    for move in moves:
        n, move_from, move_to = map(int, re.findall(r"\d+", move))
        move_from, move_to = move_from - 1, move_to - 1
        items = list(filter(lambda x: x != '', columns[move_from]))[:n][::-1]
        columns[move_to] = items + list(filter(lambda x: x != '', columns[move_to]))
        columns[move_from] = columns[move_from][n:]
    print("".join(map(lambda x: x[0], columns)).replace("[", "").replace("]", ""))

if __name__ == "__main__":
    main()