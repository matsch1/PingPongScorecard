from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class LayoutButtons(GridLayout):
    def __init__(self,layout, **kwargs):
        super().__init__(**kwargs)
        self.layout = layout
        self.cols = 1

        self.reset_button = Button(text="New Game", size_hint=(0.5, 0.2), size=(50,20))
        self.reset_button.border = (10, 10, 5, 5)
        self.reset_button.bind(on_press=self.on_button_pressed)
        self.add_widget(self.reset_button)

    def on_button_pressed(self, instance):
        self.layout.controller.reset_scores()
        for index_player in range(0,self.layout.controller.model.number_of_players):
            self.layout.layout_players[index_player].player_score.text = str(self.layout.controller.model.players[index_player].score)

