# main.py

from kivy.app import App

from Model import Model
from Controller import Controller
from Layout import View



class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    def build(self):
        model = Model()
        controller = Controller(model)
        view = View(controller)
        return view


if __name__ == '__main__':
    MyApp().run()
