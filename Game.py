import numpy as np
import pygame
import sys
import time
from pygame import locals
from clsTicTacToe import TicTacToe


class Game:
    AI = TicTacToe.AI
    AI_TEXT = "AI"
    Human = TicTacToe.HUMAN
    HUMAN_TEXT = "Human"
    Not_PLAYED = TicTacToe.NOT_PLAYED
    turn = HUMAN_TEXT
    width = 400
    height = 400
    white = (255, 255, 255)
    blue = (0, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    black = (0, 0, 0)
    fps = 30

    def __init__(self):
        pygame.init()

        self.board = np.zeros((3, 3)).astype("int")
        self.CLOCK = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height + 100), 0, 32)
        pygame.display.set_caption("My Tic Tac Toe")
        self.coverImage = pygame.image.load("Cover.png")
        self.humanImage = pygame.image.load("X.png")
        self.AiImage = pygame.image.load("O.png")
        self.coverImage = pygame.transform.scale(
            self.coverImage, (self.width, self.height + 100)
        )
        self.humanImage = pygame.transform.scale(self.humanImage, (80, 80))
        self.AiImage = pygame.transform.scale(self.AiImage, (80, 80))
        self.gameInitiatingWindow()
        self.drawStatus()

    def gameInitiatingWindow(self):
        self.screen.blit(self.coverImage, (0, 0))
        pygame.display.update()
        time.sleep(1)
        self.screen.fill(self.white)
        pygame.draw.line(
            self.screen,
            self.black,
            (self.width / 3, 0),
            (self.width / 3, self.height),
            7,
        )
        pygame.draw.line(
            self.screen,
            self.black,
            (self.width / 3 * 2, 0),
            (self.width / 3 * 2, self.height),
            7,
        )
        pygame.draw.line(
            self.screen,
            self.black,
            (0, self.height / 3),
            (self.width, self.height / 3),
            7,
        )
        pygame.draw.line(
            self.screen,
            self.black,
            (0, self.height / 3 * 2),
            (self.width, self.height / 3 * 2),
            7,
        )

    def drawStatus(self):
        AI_Game = TicTacToe(self.board)
        evalBoard = AI_Game.evaluate()
        isMovesRemain = AI_Game.is_moves_remain()
        reset = False
        color = self.white

        if evalBoard == AI_Game.SCORE_WIN:
            message = "AI wins."
            color = self.yellow
            reset = True
        elif evalBoard == AI_Game.SCORE_LOOSE:
            message = "Human wins."
            color = self.green
            reset = True
        elif evalBoard == AI_Game.SCORE_DRAW:
            if isMovesRemain:
                message = self.turn + "'s turn."
            else:
                message = "Game Draw !"
                color = self.blue
                reset = True

        font = pygame.font.Font(None, 30)
        text = font.render(message, 1, color)
        self.screen.fill((0, 0, 0), (0, 400, 500, 100))
        text_rect = text.get_rect(center=(self.width / 2, 500 - 50))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        if reset:
            self.resetGame()

    def drawXO(self, row, col, turn):
        posx = self.width / 3 * row + 30
        posy = self.height / 3 * col + 30

        if turn == self.AI_TEXT:
            self.screen.blit(self.AiImage, (posy, posx))
            self.board[row, col] = TicTacToe.AI
            self.turn = self.HUMAN_TEXT
        elif turn == self.HUMAN_TEXT:
            self.screen.blit(self.humanImage, (posy, posx))
            self.board[row, col] = TicTacToe.HUMAN
            self.turn = self.AI_TEXT

        self.drawStatus()
        pygame.display.update()

    def playAI(self):
        AI_Game = TicTacToe(self.board)
        row, col, _ = AI_Game.find_best_move()
        if self.board[row, col] == TicTacToe.NOT_PLAYED:
            self.drawXO(row, col, self.AI_TEXT)

    def playUser(self):
        x, y = pygame.mouse.get_pos()

        if x < self.width / 3:
            col = 0
        elif x < self.width / 3 * 2:
            col = 1
        elif x < self.width:
            col = 2
        else:
            col = None

        if y < self.height / 3:
            row = 0
        elif y < self.height / 3 * 2:
            row = 1
        elif y < self.height:
            row = 2
        else:
            row = None

        if col is not None and row is not None:
            if self.board[row, col] == TicTacToe.NOT_PLAYED:
                self.drawXO(row, col, self.HUMAN_TEXT)

    def resetGame(self):
        time.sleep(3)
        self.turn = self.HUMAN_TEXT
        self.gameInitiatingWindow()
        self.board = np.zeros((3, 3)).astype("int")
        self.drawStatus()

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == locals.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == locals.MOUSEBUTTONDOWN:
                    if self.turn == self.HUMAN_TEXT:
                        self.playUser()

            if self.turn == self.AI_TEXT:
                self.playAI()

            pygame.display.update()
            self.CLOCK.tick(self.fps)


if __name__ == "__main__":
    game = Game()
    game.play()
