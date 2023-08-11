from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window


class MainWindow(Screen):
    def __init__(self, controller, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.controller = controller
        # Window.clearcolor = (0, 0.6, 0.1, 1.0)
        if self.controller.debug:
            self.window_size_old = Window.size
            self.window_size_new = [1334/2, 750/2]
            Window.size = (self.window_size_new)

        self.LayoutMain = LayoutMain(self)
        self.add_widget(self.LayoutMain)


class LayoutMain(BoxLayout):
    def __init__(self, main_screen):
        super(LayoutMain, self).__init__()
        self.main_screen = main_screen
        self.orientation = 'vertical'
        self.spacing = 10

        self.__add_widgets()

    def __add_widgets(self):
        self.subgrid_players = GridLayout(
            cols=self.main_screen.controller.model.number_of_players)
        self.subgrid_players.spacing = 10
        self.layout_players = []
        for index_player in range(self.main_screen.controller.model.number_of_players):
            self.layout_players.append(LayoutPlayer(self, index_player))
            self.subgrid_players.add_widget(self.layout_players[index_player])
        self.add_widget(self.subgrid_players)

        self.add_widget(LayoutButtons(self))

    def button_pressed_new_game(self, instance):
        self.main_screen.controller.reset_scores()
        self.update_layout_score(instance)

    def button_pressed_reset_all(self, instance):
        self.main_screen.controller.reset_wins()
        self.__update_layout_wins(instance)

        self.main_screen.controller.reset_scores()
        self.update_layout_score(instance)

    def button_pressed_settings(self, instance):
        self.app = App.get_running_app()
        self.app.screen_manager.current = "settings_screen"
        self.app.screen_manager.transition.direction = "left"

    def change_player_name(self, name, index_player):
        self.layout_players[index_player].set_name_text(name)

    def __update_layout_wins(self, instance):
        for index_player in range(0, self.main_screen.controller.model.number_of_players):
            self.layout_players[index_player].update_points_text('wins')

    def update_layout_score(self, instance):
        for index_player in range(0, self.main_screen.controller.model.number_of_players):
            self.layout_players[index_player].update_points_text('score')


class LayoutPlayer(GridLayout):
    def __init__(self, LayoutMain, index_player):
        super(LayoutPlayer, self).__init__()
        self.cols = 1
        self.spacing = 5

        self.LayoutMain = LayoutMain
        self.index_player = index_player

        self.__add_widgets()

    def __add_widgets(self):
        self.player_name = Label(
            text=self.LayoutMain.main_screen.controller.model.player[self.index_player].name, font_size=48)

        self.add_widget(self.player_name)

        self.player_wins = Label()
        self.update_points_text('wins')
        self.player_score = Label(font_size=32)
        self.update_points_text('score')

        self.PointsLayout = GridLayout(cols=2)
        self.PointsLayout.add_widget(self.player_wins)
        self.PointsLayout.add_widget(self.player_score)
        self.add_widget(self.PointsLayout)

        self.button_increment = Button(
            text="+1", font_size="20sp", background_color=self.LayoutMain.main_screen.controller.model.colors["button"], size_hint_x=0.7, size_hint_y=1)
        self.button_increment.bind(on_press=self.button_pressed_increment)
        self.button_decrement = Button(
            text="-1", font_size="20sp", background_color=self.LayoutMain.main_screen.controller.model.colors["button"], size_hint_x=0.3, size_hint_y=1)
        self.button_decrement.bind(on_press=self.button_pressed_decrement)
        self.ButtonPointsLayoutLayout = GridLayout(cols=2)
        self.ButtonPointsLayoutLayout.add_widget(self.button_increment)
        self.ButtonPointsLayoutLayout.add_widget(self.button_decrement)
        self.add_widget(self.ButtonPointsLayoutLayout)

    def button_pressed_increment(self, instance):
        self.wins_old = self.LayoutMain.main_screen.controller.model.player[
            self.index_player].wins.get()

        self.LayoutMain.main_screen.controller.increment_score(
            self.index_player)
        self.update_points_text('score')

        self.__check_if_one_player_wins(instance)

    def __check_if_one_player_wins(self, instance):
        if self.wins_old != self.LayoutMain.main_screen.controller.model.player[self.index_player].wins.get():
            if self.LayoutMain.main_screen.controller.model.sound_activated:
                self.LayoutMain.main_screen.controller.speaker.say_text(
                    'Congratulations, you win')
            self.popup = Alert(style='Info', title='Congratulations ' + self.LayoutMain.main_screen.controller.model.player[self.index_player].name + '!',
                               text='YOU WIN!', button_text='Close and New Game')
            self.update_points_text('wins')

            self.LayoutMain.main_screen.controller.reset_scores()
            self.LayoutMain.update_layout_score(instance)

    def button_pressed_decrement(self, instance):
        self.LayoutMain.main_screen.controller.decrement_score(
            self.index_player)
        self.update_points_text('score')

    def update_points_text(self, usecase):
        if usecase == 'score':
            self.player_score.text = 'Score: ' + str(self.LayoutMain.main_screen.controller.model.player[self.index_player].score.get(
            ))
        elif usecase == 'wins':
            self.player_wins.text = 'Wins: ' + str(self.LayoutMain.main_screen.controller.model.player[self.index_player].wins.get(
            ))

    def set_name_text(self, name):
        self.player_name.text = name


class LayoutButtons(GridLayout):
    def __init__(self, LayoutMain, **kwargs):
        super().__init__(**kwargs)
        self.LayoutMain = LayoutMain
        self.cols = 3
        # self.font_size=32
        self.size_hint_y = 0.15
        # self.height=50
        self.size_hint_x = 1
        # self.width=200

        self.new_game = Button(text="New Game", size_hint_x=1, size_hint_y=1.5)
        self.new_game.bind(on_press=self.LayoutMain.button_pressed_new_game)
        self.add_widget(self.new_game)

        self.reset_wins = Button(text="Reset All")
        self.reset_wins.bind(on_press=self.LayoutMain.button_pressed_reset_all)
        self.add_widget(self.reset_wins)

        self.settings = Button(text="Settings")
        self.settings.bind(on_press=self.LayoutMain.button_pressed_settings)
        self.add_widget(self.settings)

############


class Alert(Popup):

    def __init__(self, style, title, text, button_text):
        super(Alert, self).__init__()
        content = GridLayout(cols=1)
        content.add_widget(
            Label(text=text)
        )
        ok_button = Button(text=button_text)
        content.add_widget(ok_button)

        if style == "Info":
            ok_button.background_color = (0.4, 0.9, 0, 1)
        elif style == "Warning":
            ok_button.background_color = (1, 0.6, 0.1, 1)
        elif style == "Error":
            ok_button.background_color = (1, 0, 0, 1)

        else:
            ValueError("Invalid Popup Style")

        popup = Popup(
            title=title,
            content=content,
            size_hint=(None, None),
            size=(Window.width / 3, Window.height / 3),
            auto_dismiss=True,
        )
        ok_button.bind(on_press=popup.dismiss)
        popup.open()
