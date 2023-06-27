from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, FadeTransition

class MainWindow(Screen):
    def __init__(self,controller, **kwargs):
        super(MainWindow,self).__init__(**kwargs)
        self.LayoutMain = LayoutMain(controller)
        self.add_widget(self.LayoutMain)


class LayoutMain(GridLayout):
    def __init__(self, controller):
        super(LayoutMain, self).__init__()
        self.controller = controller

        self.cols = 1
        self.subgrid = GridLayout()
        self.subgrid.cols = controller.model.number_of_players
        self.add_widget(self.subgrid)
        
        self.layout_players = []
        for index_player in range(controller.model.number_of_players):
            self.layout_players.append(LayoutPlayer(self,index_player))
            self.subgrid.add_widget(self.layout_players[index_player])

        self.add_widget(LayoutButtons(self))

    def press_new_game(self, instance):
        self.controller.reset_scores()
        for index_player in range(0,self.controller.model.number_of_players):
            self.layout_players[index_player].player_score.text = self.layout_players[index_player].update_score(self.controller.model.players[index_player].score)

    def press_reset_all(self, instance):
        self.controller.reset_wins()
        for index_player in range(0,self.controller.model.number_of_players):
            self.layout_players[index_player].player_wins.text = self.layout_players[index_player].update_wins(self.controller.model.players[index_player].wins)
        self.press_new_game(instance)

    def press_settings(self, instance):
        self.app = App.get_running_app()
        self.app.screen_manager.current="settings_screen"
        self.app.screen_manager.transition.direction="left"

    def change_player_name(self, name, index_player):
        self.layout_players[index_player].set_name(name.text)


###################

class LayoutPlayer(GridLayout):
    def __init__(self, layout,index_player):
        self.layout = layout
        self.index_player = index_player
        super(LayoutPlayer, self).__init__()
        self.cols = 1

        self.player_name = Label(text=self.layout.controller.model.players[self.index_player].name)
        self.add_widget(self.player_name)

        self.player_wins = Label(text = "Wins: 0")
        self.add_widget(self.player_wins)

        self.player_score = Label(text = "Points: 0")
        self.add_widget(self.player_score)

        self.button_increment = Button(text="+1")
        self.button_increment.bind(on_press=self.press_increment)
        self.add_widget(self.button_increment)

        self.button_decrement = Button(text="-1")
        self.button_decrement.bind(on_press=self.press_decrement)
        self.add_widget(self.button_decrement)

    def press_increment(self,instance):
        wins_old = self.layout.controller.model.players[self.index_player].wins

        self.layout.controller.score_increment(self.index_player)
        self.player_score.text = self.update_score(self.layout.controller.model.players[self.index_player].score)

        if wins_old != self.layout.controller.model.players[self.index_player].wins:
            #winner popup
            "You Win - Start new game"
            self.player_wins.text = self.update_wins(self.layout.controller.model.players[self.index_player].wins)
            self.layout.press_new_game(instance)

    def press_decrement(self,instance):
        self.layout.controller.score_decrement(self.index_player)
        self.player_score.text = self.update_score(self.layout.controller.model.players[self.index_player].score)

    def update_score(self, score):
        return 'Points: ' + str(score)
    
    def update_wins(self, wins):
        return 'Wins: ' + str(wins)
    
    def set_name(self, name):
        self.player_name.text = name
    
############

class LayoutButtons(GridLayout):
    def __init__(self,layout, **kwargs):
        super().__init__(**kwargs)
        self.layout = layout
        self.cols = 3

        self.new_game = Button(text="New Game")
        self.new_game.bind(on_press=self.layout.press_new_game)
        self.add_widget(self.new_game)

        self.reset_wins = Button(text="Reset All")
        self.reset_wins.bind(on_press=self.layout.press_reset_all)
        self.add_widget(self.reset_wins)

        self.settings = Button(text="Settings")
        self.settings.bind(on_press=self.layout.press_settings)
        self.add_widget(self.settings)