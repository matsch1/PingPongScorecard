from Player import Player

class Model:
    def __init__(self):
        self.number_of_players = 2
        self.players = []

        for index_player in range(self.number_of_players):
            self.players.append(Player(index_player))