from collections import Counter
from util import read_input
from dataclasses import dataclass

@dataclass
class Lanternfish:
    timer: int = 8

def simulate_spawn(inital_fish_timer_list, days=18):
    fish_school = [Lanternfish(t) for t in inital_fish_timer_list]
    for _ in range(days):
        for fish in fish_school.copy():
            fish.timer -=1
            if fish.timer == -1:
                fish.timer = 6
                fish_school.append(Lanternfish(8))
    return len(fish_school)

def simulate_spawn_fast(initial_fish_timer_list, days=18):
    fish_school = Counter()
    fish_school.update(initial_fish_timer_list)
    for _ in range(days):
        for i in range(0, 9):
            fish_school[i-1] = fish_school[i]
        fish_school[8] = 0
        fish_school[6] += fish_school[-1]
        fish_school[8] += fish_school[-1]
        fish_school[-1] = 0    
    return sum(fish_school.values())

if __name__ == "__main__":
    test_data = read_input("day6", single_line=True, test=True, as_int=True)
    assert simulate_spawn_fast(test_data, days=80) == 5934
    data = read_input("day6", single_line=True, as_int=True)
    print(f"Part 1: {simulate_spawn_fast(data, days=80)}")
    assert simulate_spawn_fast(test_data, days=256) == 26984457539
    print(f"Part 2: {simulate_spawn_fast(data, days=256)}")