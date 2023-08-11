from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox

from PingPongScorecard.MainWindow import Alert


class SettingsWindow(Screen):
    def __init__(self, main_screen, **kwargs):
        super().__init__(**kwargs)
        self.main_screen = main_screen

        self.LayoutSettings = SettingsLayout(self)
        self.add_widget(self.LayoutSettings)


class SettingsLayout(GridLayout):
    def __init__(self, settings_screen):
        super(SettingsLayout, self).__init__()
        self.settings_screen = settings_screen
        self.cols = 1

        self.__add_widgets()

    def __add_widgets(self):
        self.subgrid = GridLayout(cols=1)
        self.subgrid.spacing = 5
        self.player_settings = []
        for index_player in range(0, self.settings_screen.main_screen.controller.model.number_of_players):
            self.player_settings.append(PlayerSettings(self, index_player))
            self.subgrid.add_widget(self.player_settings[index_player])

        self.MaxScoreNumberLayout = GridLayout(cols=2)
        self.MaxScoreNumberLayout.TextInput = FormattedTextInput(
            self.settings_screen.main_screen.controller.model.max_score_number, debug=self.settings_screen.main_screen.controller.debug)
        self.MaxScoreNumberLayout.TextInput.bind(
            on_text_validate=self.button_pressed_change_max_score_number)
        self.MaxScoreNumberLayout.submit = Button(
            text="change score for winning the game", background_color=self.settings_screen.main_screen.controller.model.colors["button"])
        self.MaxScoreNumberLayout.submit.bind(
            on_press=self.button_pressed_change_max_score_number)
        self.MaxScoreNumberLayout.add_widget(
            self.MaxScoreNumberLayout.TextInput)
        self.MaxScoreNumberLayout.add_widget(self.MaxScoreNumberLayout.submit)
        self.subgrid.add_widget(self.MaxScoreNumberLayout)

        self.SoundLayout = GridLayout(cols=2)
        self.SoundLayout.Label = Label(text="Activate Sounds")
        self.SoundLayout.CB = CheckBox(
            active=self.settings_screen.main_screen.controller.model.sound_activated, color=(1, 1, 0))
        # self.SoundLayout.CB.bind(active = self.soundCB_active) # Funktionalität auskommentiert, da nicht lauffähig unter meiner Windows Verison, Ubunut i.O,
        self.SoundLayout.add_widget(self.SoundLayout.Label)
        self.SoundLayout.add_widget(self.SoundLayout.CB)
        self.subgrid.add_widget(self.SoundLayout)

        self.add_widget(self.subgrid)

        self.ReturnButton = Button(
            text="Back", size_hint_x=1, size_hint_y=0.15)
        self.ReturnButton.bind(on_press=self.button_pressed_return)
        self.add_widget(self.ReturnButton)

    def button_pressed_return(self, instance):
        self.app = App.get_running_app()
        self.app.screen_manager.current = "main_screen"
        self.app.screen_manager.transition.direction = "right"

    def button_pressed_change_max_score_number(self, instance):
        new_score_number = int(self.MaxScoreNumberLayout.TextInput.text)
        if new_score_number > 0 and new_score_number < 100:
            self.settings_screen.main_screen.controller.model.max_score_number = new_score_number
        else:
            self.MaxScoreNumberLayout.TextInput.text = str(
                self.settings_screen.main_screen.controller.model.max_score_number)
            Alert(style='Warning', title='oops!',
                  text='Invalid Max Score Number', button_text='Ok')

    def soundCB_active(self, instance, isActive):
        if isActive:
            self.settings_screen.main_screen.controller.model.sound_active = True
        else:
            self.settings_screen.main_screen.controller.model.sound_active = False


class PlayerSettings(GridLayout):
    def __init__(self, SettingsLayout, index_player) -> None:
        super(PlayerSettings, self).__init__()
        self.SettingsLayout = SettingsLayout
        self.cols = 2
        self.index_player = index_player

        self.name = FormattedTextInput(
            text=SettingsLayout.settings_screen.main_screen.controller.model.player[index_player].name, debug=self.SettingsLayout.settings_screen.main_screen.controller.debug)
        self.name.bind(on_text_validate=self.change_player_name)
        self.submit = Button(
            text="change name", background_color=self.SettingsLayout.settings_screen.main_screen.controller.model.colors["button"])
        self.submit.bind(on_press=self.change_player_name)
        self.add_widget(self.name)
        self.add_widget(self.submit)

    def change_player_name(self, instance):
        new_player_name = self.name.text
        if len(new_player_name) < 20:
            self.SettingsLayout.settings_screen.main_screen.controller.model.player[
                self.index_player].name = new_player_name
            self.SettingsLayout.settings_screen.main_screen.LayoutMain.change_player_name(
                new_player_name, self.index_player)
        else:
            self.name.text = self.SettingsLayout.settings_screen.main_screen.controller.model.player[
                self.index_player].name
            Alert(style='Warning', title='oops!',
                  text='Invalid Player Name', button_text='Ok')


class FormattedTextInput(TextInput):
    def __init__(self, text, debug=False) -> None:
        super(FormattedTextInput, self).__init__()
        self.halign = "center"
        self.multiline = False

        if debug:
            self.padding_y = [self.height / 2.0 * 800/1334 -
                              (self.line_height / 2.0 * 800/1334), 0]
        else:
            self.padding_y = [self.height / 2.0 -
                              (self.line_height / 2.0), 0]

        self.text = str(text)
