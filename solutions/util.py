def read_input(path, as_int=False):
    with open(path) as f:
        puzzle_input = f.read().splitlines()
    if as_int:
        puzzle_input = [int(n) for n in puzzle_input]
    return puzzle_input