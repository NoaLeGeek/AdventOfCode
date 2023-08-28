from copy import copy

import Utils
import re


def main():
    data = Utils.read_input()
    length = 14
    index = 0
    for i in range(len(data)-length-1):
        if len(set(data[i:i+length])) == length:
            index += length
            break
        else:
            index += 1
    print(index)

if __name__ == "__main__":
    main()