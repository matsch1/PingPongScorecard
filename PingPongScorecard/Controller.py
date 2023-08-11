import pyttsx3
from kivy.core.window import Window


class Controller:
    def __init__(self, model):
        self.model = model
        self.speaker = Speaker(self.model.language)
        self.debugger = Debugger(self.model.debug_active)

    def increment_score(self, index_player):
        self.model.player[index_player].score.increment()

        if self.model.player[index_player].score.get() == self.model.max_score_number:
            self.win_game(index_player)

    def decrement_score(self, index_player):
        if self.model.player[index_player].score.get() > 0:
            self.model.player[index_player].score.decrement()

    def win_game(self, index_player):
        self.model.player[index_player].wins.increment()

    def reset_scores(self):
        for index_player in range(0, len(self.model.player)):
            self.model.player[index_player].score.set(0)

    def reset_wins(self):
        for index_player in range(0, len(self.model.player)):
            self.model.player[index_player].wins.set(0)


class Speaker():
    def __init__(self, language) -> None:
        self.engine = pyttsx3.init()
        self.voice_name = ""
        try:
            self.change_voice(language)
        except:
            print(language + " is not available: use default language\n")

    def change_voice(self, language):
        for voice in self.engine.getProperty('voices'):
            if voice.name.find(language) > 0:
                self.engine.setProperty('voice', voice.id)
                self.voice_name = voice.name
                return True
        raise ValueError("Invalid Language: " + language)

    def say_text(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


class Debugger():
    def __init__(self, debug_active) -> None:
        self.active = debug_active

    def rescale_windowsize(self) -> None:
        self.window_size_old = Window.size
        # typical smartphone size (16:9) divided by 2 for better view on screen
        self.window_size_new = [1334/2, 750/2]
        Window.size = (self.window_size_new)
