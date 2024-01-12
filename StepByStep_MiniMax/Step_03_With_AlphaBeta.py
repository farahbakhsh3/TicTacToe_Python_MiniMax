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

# All winnig state in TicTacToe, if all cells filled with a same player,
# it is a winning state
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


def minimax(board, isMax, depth, alpha, beta):
    """
    Run minimax algorithm
    """
    score = evaluate(board)

    if score == SCORE_WIN:
        return SCORE_WIN - depth
    if score == SCORE_LOOSE:
        return SCORE_LOOSE + depth
    if score == SCORE_DRAW:
        if not is_moves_remain(board):
            return SCORE_DRAW

    if isMax:
        best = SCORE_MIN
        for row in range(BOARD_ROW):
            for col in range(BOARD_COL):
                if board[row, col] == NOT_PLAYED:
                    board[row, col] = AI
                    score = minimax(board, isMax=False, depth=depth+1,
                                    alpha=alpha, beta=beta)
                    best = np.max((score, best))
                    alpha = np.max((alpha, best))
                    board[row, col] = NOT_PLAYED
                    if beta <= alpha:
                        break
        return best
    else:
        best = SCORE_MAX
        for row in range(BOARD_ROW):
            for col in range(BOARD_COL):
                if board[row, col] == NOT_PLAYED:
                    board[row, col] = HUMAN
                    score = minimax(board, isMax=True, depth=depth+1,
                                    alpha=alpha, beta=beta)
                    best = np.min((score, best))
                    beta = np.min((beta, best))
                    board[row, col] = NOT_PLAYED
                    if alpha >= beta:
                        break
        return best


def find_best_move(board):
    """
    For all empty cells,
    fill empty cell with AI
    and calculate minimax value
    then choose best value
    """
    best_row, best_col, best_score = -1, -1, SCORE_MIN
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            if board[row, col] == NOT_PLAYED:
                board[row, col] = AI
                move_score = minimax(board, isMax=False, depth=0,
                                     alpha=SCORE_MIN, beta=SCORE_MAX)
                board[row, col] = NOT_PLAYED
                if move_score > best_score:
                    best_row = row
                    best_col = col
                    best_score = move_score
    return best_row, best_col, best_score


if __name__ == "__main__":
    board = np.array((
        [1, 2, 0],
        [0, 2, 0],
        [0, 0, 0]
    ))
    print_board(board)
    best_row, best_col, best_score = find_best_move(board)
    print(
        f"best_row: {best_row}\n"
        + f"best_col: {best_col}\n"
        + f"best_score: {best_score}"
    )
