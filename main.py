def read_input_as_int(path):
    with open(path, "r") as f:
        return [int(n.strip()) for n in f.readlines()]
