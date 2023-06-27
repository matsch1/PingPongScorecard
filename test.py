
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.uix.navigationdrawer import MDNavigationDrawer
#from kivymd.uix.toolbar import MDToolbar

class ParentScreen1(Screen):
    def __init__(self,**kwargs):
        super(ParentScreen1,self).__init__(**kwargs)
        box1 = BoxLayout(orientation ='vertical')
        box1.add_widget(MDLabel(text="Label in BoxLayout in ParentScreen1",
            pos_hint={'center_x':.95}))
        button1 = Button(text="Button(ParentScreen1)")
        button1.bind(on_press=self.change_screen)
        box1.add_widget(button1)
        self.add_widget(box1)

    def change_screen(self,instance):
        print('this work')
        self.app = MDApp.get_running_app()
        self.app.psm.current="ps2"


class ParentScreen2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        super_box=BoxLayout(orientation ='vertical')
        csm=ScreenManager()
        cs1=ChildScreen1(name="child_screen1")
        cs2=ChildScreen2(name="child_screen2")
        csm.add_widget(cs1)
        csm.add_widget(cs2)
        csm.current="child_screen1"
        self.csm=csm
#Add navigation buttons
        nav_drawer=MDNavigationDrawer()
        self.nav_drawer=nav_drawer
        nav_box=BoxLayout(orientation ='vertical',size_hint=(0.1,0.9))
        nav_button1 = Button(text="Button(Nav) go to childS2")
        nav_button1.bind(on_press=self.nav_change_screen1)
        nav_button2 = Button(text="Button(Nav) go to childS1")
        nav_button2.bind(on_press=self.nav_change_screen2)
        nav_box.add_widget(nav_button1)
        nav_box.add_widget(nav_button2)
        nav_drawer.add_widget(nav_box)
        self.add_widget(nav_drawer)
        # #add navigation toolbar
        #toolbar=MDToolbar(title="App Toolbar", size_hint=(1,0.1))
        #toolbar.left_action_items=[["arrow-left", lambda x: nav_drawer.set_state("open")]]

        #super_box.add_widget(toolbar)
        super_box.add_widget(csm)
        self.add_widget(super_box)


    def nav_change_screen1(self,instance):
        print('inside nav_change_screen1')
        self.csm.current="child_screen2"

    def nav_change_screen2(self,instance):
        print('inside nav_change_screen2')
        self.csm.current="child_screen1"

class ChildScreen1(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        box1 = BoxLayout(orientation ='vertical')
        box1.add_widget(MDLabel(text="Label in BoxLayout in ChildScreen1",
            pos_hint={'center_x':.95}))
        self.add_widget(box1)

class ChildScreen2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        box2 = BoxLayout(orientation ='vertical')
        box2.add_widget(MDLabel(text="Label in BoxLayout in ChildScreen2",
            pos_hint={'center_x':.95}))
        self.add_widget(box2)

class MainApp(MDApp):
    def build(self):
        parent_screen2=ParentScreen2()
        self.parent_screen2=parent_screen2
        psm=ScreenManager()
        self.psm=psm

        ps1=ParentScreen1(name="ps1")
        ps2=ParentScreen2(name="ps2")
        psm.add_widget(ps1)
        psm.add_widget(ps2)
        psm.current="ps1"
        print(psm.screens)
        print('self.dir::::',dir(self))
        return psm

MainApp().run()
