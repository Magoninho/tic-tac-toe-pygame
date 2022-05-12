import pygame
import json
from jogador import Jogador
from pygame.locals import *

# some constants
SCREEN_SIZE = (500, 500)
TITLE = "Tic Tac Toe"
colors = {
    "WHITE": [255, 255, 255],
    "BLACK": [21, 29, 33],
    "RED": [255, 0, 0],
    "BLUE" : [0, 0, 255]

}
pygame.font.init()

with open('./settings.json') as f:
    settings = json.load(f)


# class Player:
#     def __init__(self):
#
#         # An array that contains the players
#         self.players = [
#             'O', 'X'
#         ]
#         # the current player (this will be changed through the plays)
#         self.current_player = 1
#
#     # the function that changes the current player
#     def change_players(self):
#         if self.current_player == 0:
#             self.current_player = 1
#         elif self.current_player == 1:
#             self.current_player = 0


class Board:
    def __init__(self, screen, player_class, cols_and_rows):
        # the surface where the board will be drawned (the screen)
        self.screen = screen
        self.cols_and_rows = cols_and_rows  # how many cols and rows the grid needs
        self.board = [
            # the grid array based on the self.cols_and_rows variable
            ['' for _ in range(self.cols_and_rows)] for _ in range(self.cols_and_rows)
        ]
        self.player = player_class  # the player class, so we can make stuff with it

        # Declaring the coordinates of the mouse so we can make the use of it
        self.mouse_x = None
        self.mouse_y = None

    # The function that will determine who is the winner
    def check_winner(self, player):

        # Conditions
        """
        Here comes a lot of conditions in diferent arrays
        and if all of one of them are True, then print the winner
        """
        for col in range(len(self.board)):

            conditions_vertical = [self.board[row][col] ==
                                   player for row in range(len(self.board))]  # this is for the verticals
            conditions_horizontal = [self.board[col][row] ==
                                     player for row in range(len(self.board))]  # this is for the horizontals
            conditions_diagonal_1 = [self.board[row][row] ==
                                     player for row in range(len(self.board))]  # this is for the first diagonal
            # conditions_diagonal_2 = [self.board[col][row] ==
            # player for row in range(len(self.board) - 1, -1, -1)]  # this is for the second diagonal
            conditions_diagonal_2 = [self.board[row][len(self.board) - 1 - row] == player for row in range(len(self.board) - 1, 0, -1)]

            # TODO: tentar fazer a condição de diagonal direito, agora eu nao sei fazer por enquanto 

            # This will check if all of the conditions in one of the arrays are true using the built-in python all() function
            if all(conditions_vertical) or all(conditions_horizontal) or all(conditions_diagonal_1) or all(
                    conditions_diagonal_2):
                # print(conditions_diagonal_2)
                print(
                    f"o jogador {player} ganhou o jogo!!!\nParabéns {player}, você é muito brabo", end="")
                exit()

    # The function that draws the board
    def draw_board(self):
        self.line_thicness = 4
        self.line_color = colors['WHITE'] if settings['dark_theme'] == True else colors['BLACK']
        # this is the offset between the lines
        # calculated by the division of the width (x) and the height (y) of the screen and the length of the board
        self.x_off = SCREEN_SIZE[0] // len(self.board)
        self.y_off = SCREEN_SIZE[1] // len(self.board)

        # The code that draws the lines using the X offset and the Y offset
        # very smart calculations (nope)
        for i in range((len(self.board)) - 1):
            pygame.draw.line(
                self.screen, self.line_color, (0, (i + 1) * self.x_off), (SCREEN_SIZE[0], (i + 1) * self.y_off),
                self.line_thicness)

            for j in range(len(self.board[i]) - 1):
                pygame.draw.line(
                    self.screen, self.line_color, ((j + 1) * self.x_off, 0), ((j + 1) * self.y_off, SCREEN_SIZE[0]),
                    self.line_thicness)

    # The function for playing the game
    def play(self, mouse_pos):

        # It gets the mouse position and divides it with the x and y offset to get 0 or 1 or 2... depending of where the mouse clicked
        self.mouse_x = int(mouse_pos[0] // self.x_off)
        self.mouse_y = int(mouse_pos[1] // self.y_off)

        # It checks if the place where you clicked is empty or not
        # if it is, then mark, else, do nothing
        if self.board[self.mouse_y][self.mouse_x] == '':
            # adds to the board and X or an O (depends on the current_player variable)
            self.board[self.mouse_y][self.mouse_x] = self.player.players[self.player.current_player]
            # runs the check winner function by passing the current_player
            self.check_winner(self.player.players[self.player.current_player])
            # When the play is done (the user clicked in some spot), the turn changes
            self.player.change_players()
            self.draw_players()  # every time that a play happens, it will draw the players

    # The function that draws the players
    def draw_players(self):

        # this is some kind of offset for the drawining don't fill the spot (also it is the thicness of the 'x' player)
        lp = 120 // self.cols_and_rows

        # because of the coordinates of the mouse starts as None, I have to verify before doing something
        if self.mouse_x is not None and self.mouse_y is not None:
            # checks which player will be drawn by the value of the current_player variable
            # if it is 'X' (current_player = 0)
            if self.player.current_player == 0:

                # a lot of smart calculations (good luck understanding then)
                pygame.draw.line(
                    self.screen, colors['RED'], ((self.mouse_x) * self.x_off + lp, (self.mouse_y) * self.y_off + lp),
                    ((self.mouse_x + 1) * self.x_off - lp, (self.mouse_y + 1) * self.y_off - lp), lp)
                pygame.draw.line(
                    self.screen, colors['RED'],
                    ((self.mouse_x) * self.x_off + lp, (self.mouse_y + 1) * self.y_off - lp),
                    ((self.mouse_x + 1) * self.x_off - lp, (self.mouse_y) * self.y_off + lp), lp)

            # if it is the 'O' (current_player = 1)
            elif self.player.current_player == 1:
                pygame.draw.ellipse(self.screen, colors['BLUE'], ((
                                                                      self.mouse_x) * self.x_off + lp / 2,
                                                                  (self.mouse_y) * self.y_off + lp / 2, self.x_off - lp,
                                                                  self.y_off - lp), 0)


# The Game class


class Game:
    def __init__(self):
        # setup stuff
        self.screen = pygame.display.set_mode(SCREEN_SIZE)  # screen size
        self.title = pygame.display.set_caption(TITLE)  # window title
        self.done = False
        # a variable that gets all the keys pressed (not useful in this game)
        self.keys = pygame.key.get_pressed()
        self.clock = pygame.time.Clock()  # the pygame clock class
        self.fps = 60  # maximum frames per second
        self.Player = Jogador()  # the player class instanciated here
        # the board class instanciated here
        self.Board = Board(self.screen, self.Player, cols_and_rows=settings['grid_size'])
        # sets the background color according to the theme
        self.background_color = colors['BLACK'] if settings['dark_theme'] == True else colors['WHITE']
        # it fills the screen once, so we can draw a lot of things when we click
        self.screen.fill(self.background_color)

    # the render method, where we render the stuff we need to render when the program starts

    def render(self):
        self.Board.draw_board()  # drawining the board
        pygame.display.update()  # updating the display

    # the loop that treats the pygame events
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

    # the method that contains the main while loop (the heart of the game)
    def main_loop(self):
        self.clock.tick(self.fps)  # limits the fps
        while not self.done:
            self.event_loop()
            self.render()


# the main function
def main():
    pygame.init()  # starts pygame
    game = Game()  # instanciate the game class
    game.main_loop()  # starts the main loop


# calls the main function
if __name__ == "__main__":
    main()
