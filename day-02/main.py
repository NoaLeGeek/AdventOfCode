# A X --> Rock +1
# B Y --> Paper +2
# C Z --> Scissors +3

def main():
    INPUT_FILE = "input-full.txt"
    winning_pairs = ["A Y", "B Z", "C X"]
    score = 0
    with open(INPUT_FILE, "r") as file:
        data = file.read()
        print(data.splitlines())
        for pair in winning_pairs:
            score += data.count(pair)*6
        for line in data.splitlines():
            score += ord(line[-1])-87 + (3 if ord(line[0])+23==ord(line[-1]) else 0)
        print(score)


if __name__ == "__main__":
    main()