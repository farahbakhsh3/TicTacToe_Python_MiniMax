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


def logger(func):
    def wrapper(*args):
        if args[3]:
            print_board(args[0])
        return func(*args)
    return wrapper


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


@logger
def minimax(board, depth, isMax, verbose=False):
    score = evaluation(board)

    if score == SCORE_LOOSE:
        return score + depth
    if score == SCORE_WIN:
        return score - depth
    if score == SCORE_DRAW:
        if not is_moves_remain(board):
            return SCORE_DRAW

    if isMax:
        best = SCORE_MIN
        for row in range(BOARD_ROW):
            for col in range(BOARD_COL):
                if board[row, col] == NOT_PLAYED:
                    board[row, col] = AI
                    score = minimax(board, depth+1, False, verbose)
                    best = np.max((score, best))
                    board[row, col] = NOT_PLAYED
        return best
    else:
        best = SCORE_MAX
        for row in range(BOARD_ROW):
            for col in range(BOARD_COL):
                if board[row, col] == NOT_PLAYED:
                    board[row, col] = HUMAN
                    score = minimax(board, depth+1, True, verbose)
                    best = np.min((score, best))
                    board[row, col] = NOT_PLAYED
        return best


def print_board(board):
    print('_' * 14)
    for row in range(BOARD_ROW):
        print('|', end='')
        for col in range(BOARD_COL):
            print(board[row, col], end=' ')
        print('|')
    print('-' * 14)
    print('  Score:', evaluation(board))
    print()


def find_best_move(board, verbose):
    best_row, best_col, best_score = -1, -1, SCORE_MIN
    best_list = []
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            if board[row, col] == NOT_PLAYED:
                board[row, col] = AI
                move_score = minimax(board, 0, False, verbose)
                board[row, col] = NOT_PLAYED
                if move_score > best_score:
                    best_row = row
                    best_col = col
                    best_score = move_score
                    best_list.clear()
                if move_score == best_score:
                    best_row = row
                    best_col = col
                    best_score = move_score
                    best_list.append((best_row, best_col, best_score))

    print('Best moves list: ', best_list)
    print(f':: Find Best Move  ---  row:{best_row}, \t col:{best_col}, \
          \t Score:{best_score}')
    return (best_row, best_col)


if __name__ == '__main__':
    board = np.array(([[1], [1], [2]],
                      [[2], [2], [0]],
                      [[1], [0], [0]]))

    best_row, best_col = find_best_move(board, verbose=False)
    board[best_row, best_col] = AI
    print_board(board)
