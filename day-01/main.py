def main():
    INPUT_FILE = 'dat-01\input-full.txt'
    with open(INPUT_FILE, 'r') as file:
        data = file.read()
        print(max(map(sum, [map(int, group) for group in map(str.split, data.split('\n\n'))])))


if __name__ == '__main__':
    main()