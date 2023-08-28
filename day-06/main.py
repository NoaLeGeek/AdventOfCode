from copy import copy

import Utils
import re


def main():
    data = Utils.read_input()
    index = 0
    for i in range(len(data)-3):
        if len(set(data[i:i+4])) == 4:
            index += 4
            break
        else:
            index += 1
    print(index)

if __name__ == "__main__":
    main()