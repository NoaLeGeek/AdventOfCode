def main():
    INPUT_FILE = "input-full.txt"
    with open(INPUT_FILE, "r") as file:
        data = file.read()
        print(sum(map(lambda c: ord(c)-(38 if ord(c) < 91 else 96), map(lambda s: s.pop(), [set(filter(lambda x: x in line[:len(line)//2], line[len(line)//2:])) for line in data.splitlines()]))))


if __name__ == "__main__":
    main()