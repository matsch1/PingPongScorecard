import pytest
from PingPongScorecard.Controller import Controller, Speaker
from PingPongScorecard.Model import Model


@pytest.fixture
def model() -> Model:
    return Model()

# test class Speaker


def test_speaker_init(model) -> None:
    speaker = Speaker(model.language)


def test_speaker_init_error(capsys) -> None:
    language = "Timbuktu"
    speaker = Speaker(language)
    out, err = capsys.readouterr()
    print(out)
    assert language + " is not available: use default language\n" in out


def test_speaker_change_voice():
    language = "English"
    speaker = Speaker(language)
    assert speaker.voice_name.find(language)

    language_new = "German"
    speaker.change_voice(language_new)
    assert speaker.voice_name.find(language_new)


def test_speaker_change_voice_error():
    language = "English"
    speaker = Speaker(language)
    assert speaker.voice_name.find(language)

    language_new = "Timbuktu"
    with pytest.raises(ValueError):
        speaker.change_voice(language_new)
        assert speaker.voice_name.find(language_new)

# test class Controller


@pytest.fixture
def controller(model) -> Controller:
    return Controller(model)


def test_controller_init(controller) -> None:
    assert controller.model
    assert controller.speaker


def test_controller_increment(controller) -> None:
    index_player = 0
    old_score = controller.model.player[index_player].score.get()
    controller.increment(index_player)
    new_score = controller.model.player[index_player].score.get()
    assert old_score == new_score-1


def test_controller_increment_wrong_player_number(controller) -> None:
    index_player = 10
    old_score = controller.model.player[index_player].score.get()


def test_controller_increment_win_game(controller) -> None:
    index_player = 0
    for index_score in range(0, controller.model.max_score_number):
        controller.increment(index_player)
    assert controller.model.player[index_player].score.get(
    ) == controller.model.max_score_number
    assert controller.model.player[index_player].wins.get() == 1


def test_controller_decrement(controller) -> None:
    index_player = 0
    old_score = 3
    controller.model.player[index_player].score.set(old_score)
    controller.decrement(index_player)
    new_score = controller.model.player[index_player].score.get()
    assert old_score == new_score+1


def test_controller_decrement_zero_limit(controller) -> None:
    index_player = 0
    old_score = 0
    controller.model.player[index_player].score.set(old_score)
    controller.decrement(index_player)
    new_score = controller.model.player[index_player].score.get()
    assert old_score == new_score


def test_controller_reset_score(controller) -> None:
    for index_player in range(0, controller.model.number_of_players):
        controller.model.player[index_player].score.set(index_player)
        assert controller.model.player[index_player].score.get(
        ) == index_player
    controller.reset_scores()
    for index_player in range(0, controller.model.number_of_players):
        assert controller.model.player[index_player].score.get() == 0


def test_controller_reset_wins(controller) -> None:
    for index_player in range(0, controller.model.number_of_players):
        controller.model.player[index_player].wins.set(index_player)
        assert controller.model.player[index_player].wins.get(
        ) == index_player
    controller.reset_wins()
    for index_player in range(0, controller.model.number_of_players):
        assert controller.model.player[index_player].wins.get() == 0
