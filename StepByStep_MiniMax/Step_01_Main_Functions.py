import numpy as np

SCORE_WIN = 10
SCORE_LOOSE = -10
SCORE_DRAW = 0

AI = 1
HUMAN = 2
NOT_PLAYED = 0

# 0 1 2
# 3 4 5
# 6 7 8
BOARD_ROW = 3
BOARD_COL = 3

# All winnig state in TicTacToe, if all cells filled with a same player, it is a winning state
BOARD_WINNING = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]


def is_moves_remain(board):
    """
    Check all cells to find an empty cell
    True for remaining Empty cell
    False for full board state
    """
    for row in board:
        for col in row:
            if col == NOT_PLAYED:
                return True

    return False


def evaluate(board):
    """
    Check board and calculate Score.
    Check all wining states.
    If all cells in evere wining state filled with a same player,
    return same score
    """
    for item in BOARD_WINNING:
        human = True
        ai = True
        for idx in item:
            who_played = board[idx // BOARD_ROW, idx % BOARD_ROW]
            if who_played != AI:
                ai = False
            if who_played != HUMAN:
                human = False

        if human:
            return SCORE_LOOSE
        if ai:
            return SCORE_WIN

    return SCORE_DRAW


def print_board(board):
    """
    Print board and score
    """
    print("|" + "-" * 9 + "|")
    for row in range(BOARD_ROW):
        print("|  ", end="")
        for col in range(BOARD_COL):
            print(board[row, col] or "_", end=" ")
        print(" |")
    print("|" + "-" * 9 + "|")
    print(">> Score:", evaluate(board))
    print("-" * 11)


# TODO : minimax...


# TODO : findBestMove


if __name__ == "__main__":
    board = np.array((
        [2, 1, 2],
        [1, 2, 0],
        [1, 1, 1]
    ))
    print_board(board)
    print(is_moves_remain(board))
    print(evaluate(board))
