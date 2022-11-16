from main import read_input_2_item


def main():
    inp = read_input_2_item("input.txt")
    cords = [0, 0]
    aim = 0
    for i in inp:
        if i[0] == "forward":
            cords[1] += int(i[1])
            cords[0] += int(i[1]) * aim
        elif i[0] == "down":
            aim += int(i[1])
        elif i[0] == "up":
            aim -= int(i[1])
    print(cords)
    print(cords[0] * cords[1])


if __name__ == '__main__':
    main()
