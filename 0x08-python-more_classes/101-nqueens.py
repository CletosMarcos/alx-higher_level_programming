#!/usr/bin/python3
"""
Solves the N-queens puzzle.

Determines all possible solutions to placing
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N
    N is the board size (NxN)

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format of a list of lists
[[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys
import copy


def init_board(n: int) -> list:
    """Initializes an `n`x`n` sized chessboard with ' ' (empty spaces)."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def board_deepcopy(board: list) -> list:
    """Returns a deepcopy of a chessboard."""
    return copy.deepcopy(board)


def get_solution(board: list) -> list:
    """Returns the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def xout(board: list, row: int, col: int):
    """X out spots on a chessboard where non-attacking queens can no longer be played."""
    n = len(board)
    # X out all forward spots
    for c in range(col + 1, n):
        board[row][c] = "x"
    # X out all backward spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, n):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    for r, c in zip(range(row + 1, n), range(col + 1, n)):
        board[r][c] = "x"
    # X out all spots diagonally up to the left
    for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        board[r][c] = "x"
    # X out all spots diagonally down to the left
    for r, c in zip(range(row + 1, n), range(col - 1, -1, -1)):
        board[r][c] = "x"
    # X out all spots diagonally up to the right
    for r, c in zip(range(row - 1, -1, -1), range(col + 1, n)):
        board[r][c] = "x"


def recursive_solve(board: list, row: int, queens: int, solutions: list) -> list:
    """Recursively solves an N-queens puzzle."""
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./101-nqueens.py N")
        sys.exit(1)
    
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    
    N = int(sys.argv[1])
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(N)
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
