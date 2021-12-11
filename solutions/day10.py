from util import read_input

part_one_score_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

part_two_score_map = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

opening_pair_map = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

closing_pair_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}


def score_errors(line):
    stack = []
    openers = ["(", "[", "<", "{"]
    for ch in line:
        if ch in openers:
            stack.append(ch)
        else:
            last_opener = stack.pop()
            if last_opener != opening_pair_map[ch]:
                return part_one_score_map[ch]
    return 0

def discard_lines(data):
    for line in data.copy():
        stack = []
        openers = ["(", "[", "<", "{"]
        for ch in line:
            if ch in openers:
                stack.append(ch)
            else:
                last_opener = stack.pop()
                if last_opener != opening_pair_map[ch]:
                    data.remove(line)
                    break
                
    return data

def complete_lines(data):
    complete = []
    for line in data:
        stack = []
        openers = ["(", "[", "<", "{"]
        for ch in line:
            if ch in openers:
                stack.append(ch)
            else:
                stack.pop()
        completion = ""
        while len(stack) > 0:
            completion += closing_pair_map[stack.pop()]
        complete.append(completion)
    return complete

def score_lines(data):
    all_scores = []
    for line in data:
        line_score = 0
        for ch in line:
            line_score *= 5
            line_score += part_two_score_map[ch]   
        all_scores.append(line_score)
    return all_scores

def part1(data):
    return sum(score_errors(line) for line in data)

def part2(data):
    data = discard_lines(data)
    data = complete_lines(data)
    scores = score_lines(data)

    return sorted(scores)[len(scores)//2]


if __name__ == "__main__":
    test_data = read_input("day10", test=True)
    assert part1(test_data) == 26397
    data = read_input("day10")
    print(f"Part 1: {part1(data)}")
    assert part2(test_data) == 288957
    print(f"Part 2: {part2(data)}")