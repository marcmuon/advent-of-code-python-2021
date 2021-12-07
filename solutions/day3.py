# https://adventofcode.com/2021/day/3


from util import read_input
from collections import Counter

def part1(data):
    gamma, epsilon = "", ""
    for i in range(len(data[0])):
        ct = Counter()
        for row in data:
            ct.update(row[i])
        if ct["1"] > ct["0"]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    
    return int(gamma, 2) * int(epsilon, 2)

def _filter_nums(nums, index, match_char):
    return [num for num in nums if num[index] == match_char]

def part2(data):
    ox_nums = data
    co2_nums = data
    for i in range(len(data[0])):
        ox_nums_ct = Counter()
        co2_nums_ct = Counter()
        for row in ox_nums:
            ox_nums_ct.update(row[i])
        if len(ox_nums) == 1:
            continue
        if ox_nums_ct["1"] > ox_nums_ct["0"]:
            ox_nums = _filter_nums(ox_nums, i, "1")  
        elif ox_nums_ct["1"] == ox_nums_ct["0"]:
            ox_nums = _filter_nums(ox_nums, i, "1") 
        else:
            ox_nums = _filter_nums(ox_nums, i, "0") 
        for row in co2_nums:
            co2_nums_ct.update(row[i])
        if len(co2_nums) == 1:
            continue
        if co2_nums_ct["1"] > co2_nums_ct["0"]:
            co2_nums = _filter_nums(co2_nums, i, "0")  
        elif co2_nums_ct["1"] == co2_nums_ct["0"]:
            co2_nums = _filter_nums(co2_nums, i, "0") 
        else:
            co2_nums = _filter_nums(co2_nums, i, "1")
    return int(ox_nums[0],2) * int(co2_nums[0], 2)

if __name__ == "__main__":
    data = read_input("day3", test=True)
    assert part1(data) == 198
    full_data = read_input("day3")
    print(f"Part 1: {part1(full_data)}")
    assert part2(data) == 230
    print(f"Part 2: {part2(full_data)}")