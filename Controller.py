class Controller:
    def __init__(self, model):
        self.model = model

    def score_increment(self,index_player):
        self.model.players[index_player].score = self.model.players[index_player].score + 1
        
        if self.model.players[index_player].score == self.model.winning_points:
            self.win_game(index_player)

    def score_decrement(self,index_player):
        if self.model.players[index_player].score > 0:
            self.model.players[index_player].score = self.model.players[index_player].score - 1

    def win_game(self,index_player):
        self.model.players[index_player].wins = self.model.players[index_player].wins + 1
    
    def reset_scores(self):
        for index_player in range(0,len(self.model.players)):
            self.model.players[index_player].set_score(0)

    def reset_wins(self):
        for index_player in range(0,len(self.model.players)):
            self.model.players[index_player].set_wins(0)