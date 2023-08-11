import random


class Soundgenerator():
    def __init__(self) -> None:
        self.size_test = 0
        self.actual_sound_index = 0

    def generate_random_sounds(self):
        self.sounds = []
        for index in range(0, self.size_test):
            self.sounds.append(random.randint(-100, 100))

    def set_sounds(self, sound_array):
        self.sounds = sound_array
        self.size_test = len(sound_array)

    def print(self):
        for index, sound in enumerate(self.sounds):
            print(f"{index}: {sound}\n")

    def get_actual_sound(self, index):
        actual_sound = self.sounds[index]
        self.actual_sound_index = index
        return actual_sound


if __name__ == "__main__":
    TEST_SIZE = 10

    test_sounds = Soundgenerator()
    test_sounds.set_sounds([50, -30, 80, -20, 10, -10, 20, 10])
    test_sounds.print()
