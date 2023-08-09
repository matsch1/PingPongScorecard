class Model:
    def __init__(self):
        self.number_of_players = 2
        self.max_score_number = 11
        self.sound_active = False
        self.language = "English"  # Sprache hängt von installierten Sprachen ab

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

    def set_max_score_number(self, value):
        self.max_score_number = value


class Player():
    def __init__(self, player_index) -> None:
        self.index = player_index
        self.name = "Player " + str(player_index+1)
        self.score = Points()
        self.wins = Points()


class Points():
    def __init__(self) -> None:
        self.points = 0

    def set(self, value):
        self.points = value

    def get(self):
        return self.points

    def increment(self):
        self.points += 1

    def decrement(self):
        self.points -= 1
