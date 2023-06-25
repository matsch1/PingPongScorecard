# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Model:
    def __init__(self):
        self.button_text = 'Button'


class View(BoxLayout):
    def __init__(self, controller):
        super(View, self).__init__()
        self.orientation = 'vertical'
        self.controller = controller

        self.button = Button(text=controller.get_button_text())
        self.button.bind(on_release=self.on_button_release)
        self.add_widget(self.button)

    def on_button_release(self, instance):
        self.controller.button_pressed()


class Controller:
    def __init__(self, model):
        self.model = model

    def get_button_text(self):
        return self.model.button_text

    def button_pressed(self):
        self.model.button_text = 'Button Pressed'


class MyApp(App):
    def build(self):
        model = Model()
        controller = Controller(model)
        view = View(controller)
        return view


if __name__ == '__main__':
    MyApp().run()
