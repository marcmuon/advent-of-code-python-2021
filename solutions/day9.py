from util import read_input

# for left, right, top bottom you can transpose and run the same function
# inner is its own thing
# corner there are just 4

def transform_array(arr, check_type):
    """We want to use the same processing function to check low points
    for left/right/top/bottom. To do this, we'll transform the arrray
    so that we can apply a function to just check the "left" column's
    low points. [flip or transpose depending on check_type]

    Returns a transposition of input array filtered to 2 columns needed.
    """
    def slice_array_window(arr, n_cols=2):
        return [row[0:n_cols] for row in arr]

    if check_type == "left":
        return slice_array_window(arr)
    elif check_type == "right":
        return [[row[-1],row[-2]] for row in arr]
    elif check_type == "top":
        transpose = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
        return slice_array_window(transpose)
    elif check_type == "bottom":
        inv_transpose = [[arr[j][i] for j in range(len(arr)-1,-1,-1)] for i in range(len(arr[0])-1,-1,-1)]
        return slice_array_window(inv_transpose)
    else:
        raise ValueError("check_type must be one of 'left', 'right', 'top', 'bottom'")
    

def find_low_points(arr, check_type):
    low_points = []
        
    if check_type == "inner":
        window = arr[1:len(arr)-1]

        for line_no, line in enumerate(window, 1):
            for i in range(1, len(line)-1):
                candidate = line[i]
                if (
                    candidate < line[i-1]
                    and candidate < line[i+1]
                    and candidate < arr[line_no-1][i]
                    and candidate < arr[line_no+1][i]
                ):
                    low_points.append(line[i])
    
    elif check_type in ["top", "bottom", "left", "right"]:
        arr_window = transform_array(arr, check_type)
        low_points = []
        for line_no, line in enumerate(arr_window[1:-2], 1):  # don't include lines with corners
            candidate = line[0]
            if (
                candidate < line[1]
                and candidate < arr_window[line_no-1][0]
                and candidate < arr_window[line_no+1][0]
            ):
                low_points.append(candidate)
        
        # check corner
        corner_candidate = arr_window[0][0]
        if corner_candidate < arr_window[1][0] and corner_candidate < arr_window[0][1]:
            low_points.append(corner_candidate)

    return low_points

def part1(data):
    check_types = ["top", "bottom", "left", "right", "inner"]
    low_points_sum = 0
    for check in check_types:
        low_points = find_low_points(data, check)
        low_points_sum += sum(n+1 for n in low_points)
    return low_points_sum

def part2(data):
    pass

if __name__ == "__main__":
    test_data = read_input("day9", as_lists_of_ints=True, test=True)
    assert part1(test_data) == 15
    data = read_input("day9", as_lists_of_ints=True)
    print(f"Part 1: {part1(data)}")
    # assert  part2(test_data) == 0
    # print(f"Part 2: {part2(data)}")