from PingPongScorecard.Model import Model, Player, Points
import pytest


# test class Points


@pytest.fixture
def points() -> Points:
    return Points()


def test_points_init(points) -> None:
    assert points.points == 0


def test_points_get_value_via_method(points) -> None:
    val = points.get()
    assert val == 0


def test_points_get_value_direct(points) -> None:
    val = points.points
    assert val == 0


def test_points_set_value_via_method(points) -> None:
    points.set(3)
    val = points.get()
    assert val == 3


def test_points_set_value_direct(points) -> None:
    points.points = 3
    val = points.get()
    assert val == 3


def test_points_increment(points) -> None:
    points.set(3)
    points.increment()
    val = points.get()
    assert val == 4


def test_points_decrement(points) -> None:
    points.set(3)
    points.decrement()
    val = points.get()
    assert val == 2

# test class Player


@pytest.fixture
def player() -> Player:
    return Player(0)


def test_player_init(player):
    assert player.index == 0
    assert player.name == "Player 1"
    assert player.score.get() == 0
    assert player.wins.get() == 0

# test class Model


@pytest.fixture
def model() -> Model:
    return Model()


def test_model_init(model):
    assert model.number_of_players == 2
    assert model.max_score_number == 11
    assert model.sound_active == False
    assert model.language == "English"


def test_model_players_length(model):
    length = len(model.players)
    assert length == 2


def test_model_players_class(model):
    for player in model.players:
        assert player.score.get() == 0


def test_model_colors_exist(model):
    assert model.colors["button"]
    assert model.colors["button_text"]
    assert model.colors["background"]
    assert model.colors["text"]
