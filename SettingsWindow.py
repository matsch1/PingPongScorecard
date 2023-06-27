from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class SettingsWindow(Screen):
    def __init__(self,controller, **kw):
        super().__init__(**kw)
        self.add_widget(SettingsLayout(controller))

class SettingsLayout(GridLayout):
    def __init__(self, controller):
        super(SettingsLayout, self).__init__()
        self.cols=1

        self.Return=Button(text="Back")
        self.Return.bind(on_press = self.press_return)
        self.add_widget(self.Return)


    def press_return(self, instance):
        self.app = App.get_running_app()
        self.app.screen_manager.current="main_screen"
        self.app.screen_manager.transition.direction="right"