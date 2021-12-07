from util import read_input
from dataclasses import dataclass

@dataclass
class Lanternfish:
    timer: int = 8

def simulate_spawn(inital_fish_timer_list, days=18):
    fish_school = [Lanternfish(t) for t in inital_fish_timer_list]
    for _ in range(days):
        for fish in list(fish_school):
            fish.timer -=1
            if fish.timer == -1:
                fish.timer = 6
                fish_school.append(Lanternfish(8))
    return len(fish_school)
if __name__ == "__main__":
    test_data = read_input("day6", single_line=True, test=True, as_int=True)
    simulate_spawn(test_data, days=80) == 5934
    data = read_input("day6", single_line=True, as_int=True)
    print(f"Part 1: {simulate_spawn(data, days=80)}")
    # simulate_spawn(test_data, days=256) == 26984457539