import pytest
from domain.entities.chess import Game
from chess import Board

from domain.exceptions.chess import InvalidFenException
from domain.values.chess import Fen


def test_create_game():
    game = Game(fen=Board().fen())

    assert game.fen == Board().fen()
    assert game.moves == []

def test_create_game_with_invalid_fen():
    with pytest.raises(InvalidFenException):
        Game(fen=Fen("invalid"))

