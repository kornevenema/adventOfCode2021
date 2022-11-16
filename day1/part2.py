from main import read_input_as_int


def main():
    inp = read_input_as_int("input.txt")
    total = 0
    for i in range(0, len(inp) - 3):
        som1 = inp[i] + inp[i + 1] + inp[i + 2]
        som2 = inp[i + 1] + inp[i + 2] + inp[i + 3]
        if som2 > som1:
            total += 1
    print(total)


if __name__ == '__main__':
    main()
