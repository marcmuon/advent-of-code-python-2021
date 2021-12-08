from os import read
from util import read_input
from collections import Counter

def median(data):
    if len(data) % 2 == 1:
        return int(data[len(data)//2])
    else:
        data = sorted(data)
        midpoint = int(len(data) / 2)
        return int(sum(data[midpoint-1:midpoint+1])/2)

def fuel_cost(data):
    cost_counter = Counter()
    cost = 0
    for i in range(1, max(data)+1):
        cost += i
        cost_counter[i] = cost
    return cost_counter

def part1(data):
    median_point = median(data)
    return sum(abs(n - median_point) for n in data)

def part2(data):
    fuel_cost_map = fuel_cost(data)
    total_cost = Counter()
    for candidate in range(min(data), max(data)):
        candidate_cost = 0
        for n in data:
            candidate_cost += fuel_cost_map[abs(n - candidate)]
        total_cost[candidate] = candidate_cost
    position = [candidate for candidate, cost in total_cost.items() if cost == min(total_cost.values())][0]
    return total_cost[position]


if __name__ == "__main__":
    test_data = read_input("day7", as_int=True, single_line=True, test=True)
    assert part1(test_data) == 37
    data = read_input("day7", as_int=True, single_line=True)
    print(f"Part 1: {part1(data)}")
    assert  part2(test_data) == 168
    print(f"Part 2: {part2(data)}")
