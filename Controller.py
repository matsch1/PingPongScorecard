import pyttsx3 
import time 
 
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

    def set_winning_points(self, winning_points):
        self.model.winning_points = winning_points
    
    def say_text(self, text):
        self.speaker = pyttsx3.init() 
        self.change_voice('English')
        self.speaker.say(text)  
        self.speaker.runAndWait()
        #self.speaker.stop()
        time.sleep(3)

    def change_voice(self, language):
        for voice in self.speaker.getProperty('voices'):
            if voice.name.find(language) > 0:
                self.speaker.setProperty('voice', voice.id)
                return True
  