class Player():
    def __init__(self,player_index) -> None:
        self.index = player_index
        self.name = "Player"
        self.score = 0


    def set_score(self,index):
        self.score = index
    