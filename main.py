import pygame
import os
from pygame.locals import *
from colors import *

SCREEN_SIZE = (500, 500)
TITLE = "Tic Tac Toe"


class Player:
    def __init__(self):
        self.players = [
            'X', 'O'
        ]
        self.current_player = 0

    def change_players(self):
        if self.current_player == 0:
            self.current_player = 1
        elif self.current_player == 1:
            self.current_player = 0


class Board:
    def __init__(self, screen, cols_and_rows):
        self.screen = screen
        self.cols_and_rows = cols_and_rows
        self.board = [
            ['' for _ in range(self.cols_and_rows)] for _ in range(self.cols_and_rows)
        ]
        self.mouse_x = None
        self.mouse_y = None

    def draw_board(self):
        # TODO: COMENTAR ESSA PARTE (COMENTAR MUITO)
        self.x_off = SCREEN_SIZE[0] // len(self.board)
        self.y_off = SCREEN_SIZE[1] // len(self.board)

        for i in range((len(self.board))):
            pygame.draw.line(
                self.screen, colors['BLACK'], (0, (i + 1) * self.x_off), (SCREEN_SIZE[0], (i + 1) * self.y_off), 5)

            for j in range(len(self.board[i])):
                pygame.draw.line(
                    self.screen, colors['BLACK'], ((j + 1) * self.x_off, 0), ((j + 1) * self.y_off, SCREEN_SIZE[0]), 5)
        self.draw_players()

    def play(self, mouse_pos, player):
        self.mouse_x = int(mouse_pos[0] // self.x_off)
        self.mouse_y = int(mouse_pos[1] // self.y_off)

        player.change_players()
        self.board[self.mouse_y][self.mouse_x] = player.players[player.current_player]
        print(self.board)

    def draw_players(self):
        lp = 120 // self.cols_and_rows
        if self.mouse_x is not None and self.mouse_y is not None:
            pygame.draw.line(
                self.screen, colors['RED'], ((self.mouse_x)*self.x_off+lp, (self.mouse_y)*self.y_off+lp), ((self.mouse_x + 1)*self.x_off-lp, (self.mouse_y+1)*self.y_off-lp), 20)
            pygame.draw.line(
                self.screen, colors['RED'], ((self.mouse_x)*self.x_off + lp, (self.mouse_y + 1)*self.y_off - lp), ((self.mouse_x + 1)*self.x_off - lp, (self.mouse_y)*self.y_off + lp), 20)

        # pygame.draw.ellipse(
        #     self.screen, colors['BLUE'], (0 + lp/2, 0 + lp/2, 100, 100), 20)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.title = pygame.display.set_caption(TITLE)
        self.done = False
        self.keys = pygame.key.get_pressed()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.Board = Board(self.screen, cols_and_rows=3)
        self.Player = Player()

    def render(self):
        self.screen.fill(colors['WHITE'])
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
                self.Board.play(self.mouse, self.Player)
                self.Board.draw_players()

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
