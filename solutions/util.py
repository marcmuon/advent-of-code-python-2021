def read_input(path, test=False, as_int=False, as_lists_of_ints=False, single_line=False, sep=","):
    base_dir = "input"
    if test:
        path = f"{base_dir}/test/{path}"
    else:
        path = f"{base_dir}/{path}"
    if not path.endswith(".txt"):
        path = f"{path}.txt"
    if single_line:
        with open(path) as f:
            puzzle_input = f.read()
        puzzle_input = puzzle_input.split(sep)    
    else:
        with open(path) as f:
            puzzle_input = f.read().splitlines()
    if as_int:
        puzzle_input = [int(n) for n in puzzle_input]
    if as_lists_of_ints:
        puzzle_input = [[int(ch) for ch in line] for line in puzzle_input]
    return puzzle_input