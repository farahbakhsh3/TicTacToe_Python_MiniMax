import numpy as np


SCORE_MIN = -1000
SCORE_MAX = 1000
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
board = np.zeros((BOARD_ROW, BOARD_COL))
BOARD_WINNING = [[0, 1, 2], [3, 4, 5], [6, 7, 8], \
                 [0, 3, 6], [1, 4, 7], [2, 5, 8], \
                 [0, 4, 8], [2, 4, 6]]


def is_moves_remain(board):
    for row in board:
        for col in row:
            if col == NOT_PLAYED:
                return True

    return False


def evaluation(board):
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



# TODO : minimax...


# TODO : findBestMove


if __name__ == '__main__':
    board = np.array(([[1], [1], [2]],
                      [[2], [2], [0]],
                      [[1], [0], [0]]))


