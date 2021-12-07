from util import read_input

def read_puzzle(path, test=False):
    data = read_input(path, test)
    data = [row.split(' -> ') for row in data]
    points = []
    for p1, p2 in data:
        x1, y1 = p1.split(',')
        x2, y2 = p2.split(',')
        points.append([(int(x1), int(y1)), (int(x2), int(y2))])
    return points

def part1(data):
    board_size = max([max(max(d)) for d in data]) + 1
    marked = [[0 for j in range(board_size)] for i in range(board_size)]
    for row in data:
        (x1, y1), (x2, y2) = row
        if x1 == x2:
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            for y in range(min_y, max_y+1):
                marked[x1][y] += 1
        elif y1 == y2:
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            for x in range(min_x, max_x+1):
                marked[x][y1] += 1
        else:
            continue
    ct = 0
    for row in marked:
        for n in row:
            if n >= 2:
                ct +=1  
    return ct

if __name__ == '__main__':
    data_test = read_puzzle("day5", test=True)
    assert part1(data_test) == 5
    data = read_puzzle("day5")
    print(f"Part 1: {part1(data)}")