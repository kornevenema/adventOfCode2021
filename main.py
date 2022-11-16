def read_input_as_int(path):
    with open(path, "r") as f:
        return [int(n.strip()) for n in f.readlines()]


def read_input_2_item(path):
    with open(path, "r") as f:
        return [n.split() for n in f.readlines()]


def read_input(path):
    with open(path, "r") as f:
        return [n.strip() for n in f.readlines()]