import pygame
import os
from pygame.locals import *
from colors import *

SCREEN_SIZE = (500, 500)
TITLE = "Tic Tac Toe"


class Player:
    def __init__(self):
        self.players = [
            'O', 'X'
        ]
        self.current_player = 1

    def change_players(self):
        if self.current_player == 0:
            self.current_player = 1
        elif self.current_player == 1:
            self.current_player = 0


class Board:
    def __init__(self, screen, player_class, cols_and_rows):
        self.screen = screen
        self.cols_and_rows = cols_and_rows
        self.board = [
            ['' for _ in range(self.cols_and_rows)] for _ in range(self.cols_and_rows)
        ]
        self.available = []  # array pra checar quais spots estao disponiveis

        self.player = player_class
        self.mouse_x = None
        self.mouse_y = None

    def check_winner(self, player):

        # Vertical
        for col in range(len(self.board)):
            conditions_vertical = [self.board[row][col] ==
                                   player for row in range(len(self.board))]
            conditions_horizontal = [self.board[col][row] ==
                                     player for row in range(len(self.board))]
            conditions_diagonal_1 = [self.board[row][row] ==
                                     player for row in range(len(self.board))]
            conditions_diagonal_2 = [self.board[col][col] ==
                                     player for col in range(len(self.board))]
            if all(conditions_vertical) or all(conditions_horizontal) or all(conditions_diagonal_1) or all(conditions_diagonal_2):
                os.system("cls")
                print(
                    f"o jogador {player} ganhou o jooj!!!\nParabéns {player}, você é muito brabo", end="")

    def draw_board(self):
        self.x_off = SCREEN_SIZE[0] // len(self.board)
        self.y_off = SCREEN_SIZE[1] // len(self.board)

        for i in range((len(self.board))-1):
            pygame.draw.line(
                self.screen, colors['BLACK'], (0, (i + 1) * self.x_off), (SCREEN_SIZE[0], (i + 1) * self.y_off), 5)

            for j in range(len(self.board[i])-1):
                pygame.draw.line(
                    self.screen, colors['BLACK'], ((j + 1) * self.x_off, 0), ((j + 1) * self.y_off, SCREEN_SIZE[0]), 5)

    def play(self, mouse_pos):

        self.mouse_x = int(mouse_pos[0] // self.x_off)
        self.mouse_y = int(mouse_pos[1] // self.y_off)

        if self.board[self.mouse_y][self.mouse_x] == '':
            # adds to the board and X or an O
            self.board[self.mouse_y][self.mouse_x] = self.player.players[self.player.current_player]
            self.check_winner(self.player.players[self.player.current_player])
            self.player.change_players()
            self.draw_players()  # toda vida que ocorrer uma jogada ele vai desenhar essa jogada
            # print(self.board)

    def draw_players(self):

        lp = 120 // self.cols_and_rows

        # como as coordenadas do mouse começam como None, eu tenho que verificar antes de executar
        if self.mouse_x is not None and self.mouse_y is not None:
            # checa qual jogador será desenhado a partir da variavel current_player da classe Player
            # se for o X
            if self.player.current_player is 0:
                pygame.draw.line(
                    self.screen, colors['RED'], ((self.mouse_x)*self.x_off+lp, (self.mouse_y)*self.y_off+lp), ((self.mouse_x + 1)*self.x_off-lp, (self.mouse_y+1)*self.y_off-lp), lp)
                pygame.draw.line(
                    self.screen, colors['RED'], ((self.mouse_x) * self.x_off + lp, (self.mouse_y + 1) * self.y_off - lp), ((self.mouse_x + 1) * self.x_off - lp, (self.mouse_y) * self.y_off + lp), lp)

            # se for a bola
            elif self.player.current_player is 1:
                pygame.draw.ellipse(self.screen, colors['BLUE'], ((
                    self.mouse_x)*self.x_off + lp/2, (self.mouse_y)*self.y_off + lp/2, self.x_off - lp, self.y_off - lp), 0)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.title = pygame.display.set_caption(TITLE)
        self.done = False
        self.keys = pygame.key.get_pressed()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.Player = Player()
        self.Board = Board(self.screen, self.Player, cols_and_rows=5)
        self.screen.fill(colors['WHITE'])

    def render(self):

        self.Board.draw_board()
        pygame.display.update()

    def update(self):

        pass

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.keys = pygame.key.get_pressed()
                if self.keys[K_ESCAPE]:
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse = pygame.mouse.get_pos()
                self.Board.play(self.mouse)

    def main_loop(self):
        self.clock.tick(self.fps)
        while not self.done:
            self.event_loop()
            self.update()
            self.render()


def main():
    pygame.init()

    game = Game()
    game.main_loop()


if __name__ == "__main__":
    main()
