class Jogador:
    def __init__(self):

        # An array that contains the players
        self.players = [
            'O', 'X'
        ]
        # the current player (this will be changed through the plays)
        self.current_player = 0

    # the function that changes the current player
    def change_players(self):
        if self.current_player == 0:
            self.current_player = 1
        elif self.current_player == 1:
            self.current_player = 0