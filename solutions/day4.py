# https://adventofcode.com/2021/day/4


from util import read_input
from itertools import compress

class Board:
    def __init__(self, layout):
        assert len(layout) == len(layout[0])
        self.layout = layout

        self.all_nums = {n for row in self.layout for n in row}
        
        self.board_size = len(self.layout[0])
        self.marked = [
            [False for m in range(self.board_size)]
            for m in range(self.board_size)
        ]

    def mark_board(self, draw):
        for i, row in enumerate(self.layout):
            for j, n in enumerate(row):
                if n == draw:
                    self.marked[i][j] = True
    
    def check_win(self):
        for row in self.marked:
            if sum(row) == self.board_size:
                return True
        
        for col in [[row[j] for row in self.marked] for j in range(self.board_size)]:
            if sum(col) == self.board_size:
                return True
        
        return False
    
    def get_unmarked_sum(self):
        unmarked_sum = 0
        for row, marks in zip(self.layout, self.marked):
            unmarked_sum += sum(num for num, mark in zip(row, marks) if not mark)
        return unmarked_sum

def read_puzzle(data):
    data = read_input(data)
    draws = [int(n) for n in data[0].split(',')]
    board_list, board = [], []
    for row in data[2:]:
        if row != '':
            nums = [int(n) for n in row.split()]
            board.append(nums)
        else:
            board_list.append(board)
            board = []
    board_list.append(board)
    return draws, board_list


def part1(draws, board_list):
    boards = [Board(board) for board in board_list]
    for draw in draws:
        for board in boards:
            if draw in board.all_nums:
                board.mark_board(draw)
                if board.check_win():
                    return draw * board.get_unmarked_sum()


if __name__ == "__main__":
    draws, board_list = read_puzzle("input/test/day4.txt")
    assert part1(draws, board_list) == 4512
    draws, board_list = read_puzzle("input/day4.txt")
    print(f"Part 1: {part1(draws, board_list)}")