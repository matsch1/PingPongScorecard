class Controller:
    def __init__(self, model):
        self.model = model

    def score_increment(self,index_player):
        self.model.players[index_player].score = self.model.players[index_player].score + 1
        
        if self.model.players[index_player].score == 11:
            # Winner Popup
            pass

    def score_decrement(self,index_player):
        if self.model.players[index_player].score > 0:
            self.model.players[index_player].score = self.model.players[index_player].score - 1

    def reset_scores(self):
        for index_player in range(0,len(self.model.players)):
            self.model.players[index_player].set_score(0)