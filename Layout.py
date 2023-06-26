from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from Layout_Player import LayoutPlayer
from Layout_Buttons import LayoutButtons

class View(GridLayout):
    def __init__(self, controller):
        super(View, self).__init__()
        self.controller = controller

        self.cols = 1
        self.subgrid = GridLayout()
        self.subgrid.cols = controller.model.number_of_players
        self.add_widget(self.subgrid)
        
        self.layout_players = []
        for index_player in range(controller.model.number_of_players):
            self.layout_players.append(LayoutPlayer(controller,index_player))
            self.subgrid.add_widget(self.layout_players[index_player])

        self.add_widget(LayoutButtons(self))


