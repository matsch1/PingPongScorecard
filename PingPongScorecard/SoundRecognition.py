from SoundGenerator import Soundgenerator
from Model import Player

SOUND_OFFSET = 10


class SoundDetector():
    def __init__(self) -> None:
        self.sound_side = []

        # test sounds
        self.test_sounds = Soundgenerator()
        self.test_sounds.set_sounds(
            [50, -30, 80, -20, 10, -10, 20, 10,  # player 1 point
             50, -30, 80, -20, 5])  # player1 off

    def detect_sound(self, index):
        # test sound, should come from smartphone microphone
        return self.test_sounds.get_actual_sound(index)

    def allocate_sound_to_player(self, index):
        if self.detect_sound(index) >= SOUND_OFFSET:
            self.sound_side = 2
        elif self.detect_sound(index) <= -SOUND_OFFSET:
            self.sound_side = 1
        else:
            self.sound_side = 0  # detect off table

    def run(self, index):
        self.allocate_sound_to_player(index)
        return self.sound_side


class Match():
    def __init__(self) -> None:
        self.player = []
        self.player.append([Player(0), Player(1)])

        self.start_game()

    def start_game(self):
        if self.player.score[0] == 0 and self.player.score[0]:
            pass


class PingPongRuleChecker():
    def __init__(self) -> None:
        self.serve = True

    def evaluate(self, old_side, new_side):
        if self.serve:
            self.serve = False
        else:
            self.serve = False
            if new_side == old_side and new_side != 0:  # ins Netz gespielt oder drüber und neuer Aufschlag -> backlog
                self.serve = True
                if old_side == 1:
                    print(f"Player{2} point\n")
                    return 2
                else:
                    print(f"Player{1} point\n")
                    return 1

            if new_side != old_side and new_side != 0:  # gültiger Spielzug
                return -1

            if new_side == 0:  # Ball trifft Platte nicht
                self.serve = True
                if old_side == 1:
                    print(f"Player{2} point\n")
                    return 2
                else:
                    print(f"Player{1} point\n")
                    return 1

            else:
                ValueError('unerwarteter Spielzug')


if __name__ == "__main__":

    sound_detector = SoundDetector()
    rule_checker = PingPongRuleChecker()

    # start game
    old_side = 0
    points_player1 = 0
    points_player2 = 0
    for index, sound in enumerate(sound_detector.test_sounds.sounds):
        new_side = sound_detector.run(index)

        point = rule_checker.evaluate(old_side, new_side)
        old_side = new_side
        if point == 1:
            points_player1 += 1
        elif point == 2:
            points_player2 += 1

    print(
        f"Points Player1: {points_player1}, Points Player2: {points_player2}\n")
