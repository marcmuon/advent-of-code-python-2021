# https://adventofcode.com/2021/day/1

from util import read_input

def count_increasing_sum(data, window_size=1):
    increase_ct = 0
    prior_sum = sum(data[0: window_size])
    for i in range(0, len(data) - (window_size - 1)):
        current_sum = sum(data[i: i + window_size])
        if current_sum > prior_sum:
            increase_ct += 1
        prior_sum = current_sum
    return increase_ct


if __name__ == "__main__":
    full_data = read_input("day1", as_int=True)
    test_data = read_input("day1", test=True, as_int=True)
    
    # PART 1
    print(f"Part 1 [Test]: {count_increasing_sum(test_data, window_size=1)}")
    assert count_increasing_sum(test_data) == 7
    print(f"Part 1 [Submit]: {count_increasing_sum(full_data, window_size=1)}")
    
    # PART 2
    print(f"Part 2 [Test]: {count_increasing_sum(test_data, window_size=3)}")
    assert count_increasing_sum(test_data, window_size=3) == 5
    print(f"Part 2 [Submit]: {count_increasing_sum(full_data, window_size=3)}")