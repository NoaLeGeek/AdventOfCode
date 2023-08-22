def main():
    INPUT_FILE = "input-full.txt"
    with open(INPUT_FILE, "r") as file:
        data = file.read()
        print(sum(map(lambda c: ord(c)-(38 if ord(c) < 91 else 96), map(lambda s: s.pop(), [set(group.splitlines()[0]) & set(group.splitlines()[1]) & set(group.splitlines()[2]) for group in ['\n'.join(data.split('\n')[i:i+3]) for i in range(0, len(data.split('\n')), 3)]]))))


if __name__ == "__main__":
    main()