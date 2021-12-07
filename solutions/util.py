def read_input(path, test=False, as_int=False, single_line=False):
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
        sep = puzzle_input[1]
        puzzle_input = puzzle_input.split(sep)    
    else:
        with open(path) as f:
            puzzle_input = f.read().splitlines()
    if as_int:
        puzzle_input = [int(n) for n in puzzle_input]
    return puzzle_input