import Utils


def main():
    data = Utils.read_input()
    print(sum(sorted(list(map(sum, [map(int, group) for group in map(str.split, data.split('\n\n'))])))[-3:]))



if __name__ == '__main__':
    main()