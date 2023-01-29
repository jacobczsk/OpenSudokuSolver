import csv
import time


def create_board(filename: str) -> list:
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=",")
        board = []
        empty = 0
        for i, row in enumerate(reader):
            if row == []:
                empty += 1
                continue
            if not len(row) == 9:
                raise Exception("Cannot create a board that isn't 9x9!")
            board.append([])
            for cell in row:
                if cell == "0":
                    board[i - empty].append(None)
                else:
                    board[i - empty].append(int(cell))
        return board


def write_board(filename: str, board: list):
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(board)


def solve(board):
    start = time.perf_counter_ns()
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return board
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, (row, col), num):
            board[row][col] = num
            if solve(board) != False:
                end = time.perf_counter_ns()
                return board, (end - start) / 10**6
            board[row][col] = None
    return False


def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == None:
                return (row, col)
    return None


def is_valid(board, pos, num):
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True
