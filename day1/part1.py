from main import read_input_as_int


def main():
    inp = read_input_as_int("input.txt")
    s = 0
    total = 0
    for i in inp:
        if i > s:
            total += 1
        s = i
    print(total - 1)


if __name__ == '__main__':
    main()
