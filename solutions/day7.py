from os import read
from util import read_input

def median(data):
    if len(data) % 2 == 1:
        return int(data[len(data)//2])
    else:
        data = sorted(data)
        midpoint = int(len(data) / 2)
        return int(sum(data[midpoint-1:midpoint+1])/2)

def part1(data):
    median_point = median(data)
    return sum(abs(n - median_point) for n in data)


if __name__ == "__main__":
    test_data = read_input("day7", as_int=True, single_line=True, test=True)
    assert part1(test_data) == 37
    data = read_input("day7", as_int=True, single_line=True)
    print(f"Part 1: {part1(data)}")