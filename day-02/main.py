def main():
    INPUT_FILE = "input-full.txt"
    points = [[3, 1, 2], [1, 2, 3], [2, 3, 1]]
    score = 0
    with open(INPUT_FILE, "r") as file:
        data = file.read()
        for line in data.splitlines():
            score += 3*(ord(line[-1])-88)+points[ord(line[0])-65][ord(line[-1])-88]
        print(score)


if __name__ == "__main__":
    main()