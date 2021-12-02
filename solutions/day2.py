# https://adventofcode.com/2021/day/2

from util import read_input
from collections import Counter


def part1(data):
    counter = Counter()
    for move in [line.split() for line in data]:
        direction, amount = move
        counter.update({direction: int(amount)})
    return counter["forward"] * (counter["down"] - counter["up"])


if __name__ == "__main__":
    data = read_input("input/test/day2.txt")
    assert part1(data) == 150
    full_data = read_input("input/day2.txt")
    print(f"Part 1: {part1(full_data)}")
