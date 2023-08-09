from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from PingPongScorecard.Model import Model
from PingPongScorecard.Controller import Controller
from PingPongScorecard.MainWindow import MainWindow
from PingPongScorecard.SettingsWindow import SettingsWindow


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "PingPongScorecard"

    def build(self):
        model = Model()
        controller = Controller(model)
        main_screen = MainWindow(controller, name="main_screen")
        settings_screen = SettingsWindow(main_screen, name="settings_screen")

        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(main_screen)
        self.screen_manager.add_widget(settings_screen)
        self.screen_manager.current = "main_screen"

        return self.screen_manager


if __name__ == '__main__':
    MyApp().run()
