import pytest
import sys
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


@pytest.fixture
def controller(model) -> Controller:
    return Controller(model)


def test_controller_init(controller) -> None:
    assert controller.model
    assert controller.speaker
