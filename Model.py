from Player import Player

class Model:
    def __init__(self):
        self.number_of_players = 2
        self.winning_points = 11
        self.sound_active = False

        self.players = []
        for index_player in range(self.number_of_players):
            self.players.append(Player(index_player))

    def get_sound_active(self):
        return self.sound_active
