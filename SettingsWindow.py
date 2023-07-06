from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox

class SettingsWindow(Screen):
    def __init__(self,main_screen, **kw):
        super().__init__(**kw)
        self.add_widget(SettingsLayout(main_screen))

class SettingsLayout(GridLayout):
    def __init__(self, main_screen):
        super(SettingsLayout, self).__init__()
        self.main_screen = main_screen
        self.cols=1

        self.subgrid = GridLayout()
        #self.subgrid.size_hint_x=self.width*0.8
        #self.subgrid.size_hint_y=None
        self.subgrid.cols = 1

        self.player_settings=[]
        for index_player in range(0,self.main_screen.controller.model.number_of_players):
            self.player_settings.append(PlayerSettings(self,index_player))
            self.subgrid.add_widget(self.player_settings[index_player])
        
        self.winning_points = GridLayout()
        self.winning_points.cols = 2
        self.winning_points.winning_points = TextInput(text = str(self.main_screen.controller.model.winning_points), halign="center")
        self.winning_points.submit = Button(text = "change winning points",background_color = self.main_screen.controller.model.colors["button"])
        self.winning_points.submit.bind(on_press = self.change_winning_points)
        self.winning_points.add_widget(self.winning_points.winning_points)
        self.winning_points.add_widget(self.winning_points.submit)
        self.subgrid.add_widget(self.winning_points)

        self.sound = GridLayout()
        self.sound.cols=2
        self.sound.Label=Label(text = "Activate Sounds")
        self.sound.CB = CheckBox(active = self.main_screen.controller.model.get_sound_active, color = (1,1,0))
        self.sound.CB.bind(active = self.soundCB_active)
        self.sound.add_widget(self.sound.Label)
        self.sound.add_widget(self.sound.CB)
        #self.subgrid.add_widget(self.sound)


        self.add_widget(self.subgrid)


        self.Return=Button(text="Back",size_hint_x=1,size_hint_y=0.15)
        self.Return.bind(on_press = self.press_return)
        self.add_widget(self.Return)


    def press_return(self, instance):
        self.app = App.get_running_app()
        self.app.screen_manager.current="main_screen"
        self.app.screen_manager.transition.direction="right"

    def change_winning_points(self, instance):
        self.main_screen.controller.set_winning_points(int(self.winning_points.winning_points.text))

    def soundCB_active(self,instance,isActive):
        if isActive:
            self.main_screen.controller.model.sound_active = True
        else:
            self.main_screen.controller.model.sound_active = False


class PlayerSettings(GridLayout):
    def __init__(self,settings_layout,index_player) -> None:
        super(PlayerSettings, self).__init__()
        self.settings_layout = settings_layout

        self.cols = 2
        self.name = TextInput(text = settings_layout.main_screen.controller.model.players[index_player].name, halign="center")
        self.index_player = index_player
        self.submit = Button(text = "change name",background_color =self.settings_layout.main_screen.controller.model.colors["button"])
        self.submit.bind(on_press=self.change_name)
        self.add_widget(self.name)
        self.add_widget(self.submit)

    def change_name(self,instance):
        self.settings_layout.main_screen.controller.model.players[self.index_player].name = self.name.text
        self.settings_layout.main_screen.LayoutMain.change_player_name(self.name.text, self.index_player)
        

