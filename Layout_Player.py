from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class LayoutPlayer(GridLayout):
    def __init__(self, controller,index_player):
        self.controller = controller
        self.index_player = index_player
        super(LayoutPlayer, self).__init__()
        self.cols = 1


        self.player_name = Label(text=self.controller.model.players[self.index_player].name + " " + str(self.index_player + 1))
        self.add_widget(self.player_name)

        self.player_score = Label(text=str(self.controller.model.players[self.index_player].score))
        self.add_widget(self.player_score)

        self.button_increment = Button(text="+1")
        self.button_increment.bind(on_press=self.press_increment)
        self.add_widget(self.button_increment)

        self.button_decrement = Button(text="-1")
        self.button_decrement.bind(on_press=self.press_decrement)
        self.add_widget(self.button_decrement)

    def press_increment(self,instance):
        self.controller.score_increment(self.index_player)
        self.player_score.text = str(self.controller.model.players[self.index_player].score)

    def press_decrement(self,instance):
        self.controller.score_decrement(self.index_player)
        self.player_score.text = str(self.controller.model.players[self.index_player].score)


        

