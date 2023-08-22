import Utils


def main():
    assignment = 0
    data = Utils.read_input()
    lzt = list(map(lambda x: range(int(x.split("-")[0]), int(x.split("-")[1])+1), sum(map(lambda x: x.split(","), data.splitlines()), [])))
    for i in range(0, len(lzt), 2):
        range1, range2 = lzt[i], lzt[i+1]
        if len(range1) > len(range2):
            range1, range2 = range2, range1
        if range1.start < range2.stop and range2.start < range1.stop:
            assignment += 1
    print(assignment)


if __name__ == "__main__":
    main()