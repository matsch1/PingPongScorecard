from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class View(BoxLayout):
    def __init__(self, controller):
        super(View, self).__init__()
        self.orientation = 'vertical'
        self.controller = controller

        self.button = Button(text=controller.get_button_text())
        self.button.bind(on_press=self.on_button_pressed)
        self.button.bind(on_release=self.on_button_release)
        self.add_widget(self.button)

        self.label = Label(text=controller.get_label_text())
        self.add_widget(self.label)

    def on_button_pressed(self, instance):
        self.controller.button_pressed()
        self.label.text = self.controller.get_label_text()

    def on_button_release(self, instance):
        self.controller.button_released()
        self.label.text = self.controller.get_label_text()
