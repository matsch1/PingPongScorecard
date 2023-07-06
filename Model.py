from Player import Player

class Model:
    def __init__(self):
        self.number_of_players = 2
        self.winning_points = 11
        self.sound_active = True
        self.language = "English"

        self.players = []
        for index_player in range(self.number_of_players):
            self.players.append(Player(index_player))

        self.colors = {}
        self.colors["button"] = (1, 0.2, 0.2, 1)
        self.colors["button_text"] = (0, 0, 0, 1)
        self.colors["background"] = (1, 1, 1, 1)
        self.colors["text"] = (0, 0, 0, 1)

    def get_sound_active(self):
        return self.sound_active
