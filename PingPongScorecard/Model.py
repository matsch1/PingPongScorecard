class Model:
    def __init__(self):
        self.number_of_players = 2
        self.max_score_number = 11
        self.sound_activated = False
        self.debug_active = True
        self.language = "English"  # Sprache hängt von installierten Sprachen ab

        self.player = []
        for index_player in range(self.number_of_players):
            self.player.append(Player(index_player))

        self.colors = {}
        self.colors["button"] = (1, 0.2, 0.2, 1)
        self.colors["button_text"] = (0, 0, 0, 1)
        self.colors["background"] = (1, 1, 1, 1)
        self.colors["text"] = (0, 0, 0, 1)


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
