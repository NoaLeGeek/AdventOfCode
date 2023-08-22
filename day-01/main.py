def main():
    INPUT_FILE = 'input-full.txt'
    with open(INPUT_FILE, 'r') as file:
        data = file.read()
        print(sum(sorted(list(map(sum, [map(int, group) for group in map(str.split, data.split('\n\n'))])))[-3:]))



if __name__ == '__main__':
    main()