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
    def __init__(self, cols_and_rows):
        self.board = [
            ['' for _ in range(cols_and_rows)] for _ in range(cols_and_rows)
        ]

    def draw_board(self, screen):
        # TODO: COMENTAR ESSA PARTE (COMENTAR MUITO)
        self.x_off = SCREEN_SIZE[0] // len(self.board)
        self.y_off = SCREEN_SIZE[1] // len(self.board)

        for i in range((len(self.board))):
            pygame.draw.line(
                screen, colors['BLACK'], (0, (i + 1) * self.x_off), (SCREEN_SIZE[0], (i + 1) * self.y_off), 5)
            for j in range(len(self.board[i])):

                pygame.draw.line(
                    screen, colors['BLACK'], ((j + 1) * self.x_off, 0), ((j + 1) * self.y_off, SCREEN_SIZE[0]), 5)

                # pygame.draw.rect(screen, colors['RED'], ((
                #     j) * x_off, (i) * y_off, 144, 144))
                # THATS THE WAY THAT WE NEED TO GO WITH OMG O FUCKING DID IT
                # os.system("clear")
    def play(self, mouse_pos, player):  # TODO: player
        mouse_x = int(mouse_pos[0] // self.x_off)
        mouse_y = int(mouse_pos[1] // self.y_off)

        player.change_players()
        self.board[mouse_y][mouse_x] = player.players[player.current_player]
        print(self.board)
        

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.title = pygame.display.set_caption(TITLE)
        self.done = False
        self.keys = pygame.key.get_pressed()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.Board = Board(cols_and_rows=3)
        self.Player = Player()

    def render(self):
        self.screen.fill(colors['WHITE'])
        self.Board.draw_board(self.screen)
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
