class Player():
    def __init__(self,player_index) -> None:
        self.index = player_index
        self.name = "Player " + str(player_index+1)
        self.score = 0
        self.wins = 0

    def set_score(self,index):
        self.score = index

    def set_wins(self,index):
        self.wins = index   