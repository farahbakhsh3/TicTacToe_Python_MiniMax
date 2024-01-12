import numpy as np


class TicTacToe:
    """
    class TicTacToe
    """
    SCORE_MIN = -1000
    SCORE_MAX = 1000

    SCORE_WIN = 10
    SCORE_LOOSE = -10
    SCORE_DRAW = 0

    AI = 1
    HUMAN = 2
    NOT_PLAYED = 0

    BOARD_ROW = 3
    BOARD_COL = 3
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

    def __init__(self, board):
        self.board = board

    def is_moves_remain(self):
        """
        Check all cells to find an empty cell
        True for remaining Empty cell
        False for full board state
        """
        for row in self.board:
            for col in row:
                if col == self.NOT_PLAYED:
                    return True
        return False

    def evaluate(self):
        """
        Check board and calculate Score.
        Check all wining states.
        If all cells in evere wining state filled with a same player,
        return same score
        """
        for item in self.BOARD_WINNING:
            human = True
            ai = True
            for idx in item:
                who_played = self.board[idx // self.BOARD_ROW,
                                        idx % self.BOARD_ROW]
                if who_played != self.AI:
                    ai = False
                if who_played != self.HUMAN:
                    human = False

            if human:
                return self.SCORE_LOOSE
            if ai:
                return self.SCORE_WIN

        return self.SCORE_DRAW

    def print_board(self):
        """
        Print board and score
        """
        print("|" + "-" * 9 + "|")
        for row in range(self.BOARD_ROW):
            print("|  ", end="")
            for col in range(self.BOARD_COL):
                print(self.board[row, col] or "_", end=" ")
            print(" |")
        print("|" + "-" * 9 + "|")
        print(">> Score:", self.evaluate())
        print("-" * 11)

    def minimax(self, isMax, depth, alpha, beta):
        """
        Run minimax algorithm
        """
        score = self.evaluate()

        if score == self.SCORE_WIN:
            return self.SCORE_WIN - depth
        if score == self.SCORE_LOOSE:
            return self.SCORE_LOOSE + depth
        if score == self.SCORE_DRAW:
            if not self.is_moves_remain():
                return self.SCORE_DRAW

        if isMax:
            best = self.SCORE_MIN
            for row in range(self.BOARD_ROW):
                for col in range(self.BOARD_COL):
                    if self.board[row, col] == self.NOT_PLAYED:
                        self.board[row, col] = self.AI
                        score = self.minimax(isMax=False, depth=depth + 1,
                                             alpha=alpha, beta=beta)
                        best = np.max((score, best))
                        alpha = np.max((alpha, best))
                        self.board[row, col] = self.NOT_PLAYED
                        if beta <= alpha:
                            break
            return best
        else:
            best = self.SCORE_MAX
            for row in range(self.BOARD_ROW):
                for col in range(self.BOARD_COL):
                    if self.board[row, col] == self.NOT_PLAYED:
                        self.board[row, col] = self.HUMAN
                        score = self.minimax(isMax=True, depth=depth + 1,
                                             alpha=alpha, beta=beta)
                        best = np.min((score, best))
                        beta = np.min((beta, best))
                        self.board[row, col] = self.NOT_PLAYED
                        if alpha >= beta:
                            break
            return best

    def find_best_move(self):
        """
        For all empty cells,
        fill empty cell with AI
        and calculate minimax value
        then choose best value
        """
        best_row, best_col, best_score = -1, -1, self.SCORE_MIN
        for row in range(self.BOARD_ROW):
            for col in range(self.BOARD_COL):
                if self.board[row, col] == self.NOT_PLAYED:
                    self.board[row, col] = self.AI
                    move_score = self.minimax(isMax=False, depth=0,
                                              alpha=self.SCORE_MIN,
                                              beta=self.SCORE_MAX)
                    self.board[row, col] = self.NOT_PLAYED
                    if move_score > best_score:
                        best_row = row
                        best_col = col
                        best_score = move_score
        return best_row, best_col, best_score


if __name__ == "__main__":
    print("class TicTacToe...")
    board = np.array((
        [1, 2, 0],
        [0, 2, 0],
        [0, 0, 0]
    ))
    game = TicTacToe(board=board)
    game.print_board()
    best_row, best_col, best_score = game.find_best_move()
    print(
        f"best_row: {best_row}\n"
        + f"best_col: {best_col}\n"
        + f"best_score: {best_score}"
    )
