import pytest
from domain.exceptions.base import EmptyValueException
from domain.exceptions.chess import InvalidFenException, InvalidMoveException
from domain.values.chess import Fen, Move
import chess

def test_create_move():
    move = Move("e2e4")
    assert move.value == "e2e4"
    assert move.as_generic_type() == "e2e4"


def test_invalid_move():
    with pytest.raises(EmptyValueException):
        Move("")

    with pytest.raises(InvalidMoveException):
        Move("invalid")


def test_create_fen():
    fen = Fen(value=chess.STARTING_FEN)
    assert fen.as_generic_type() == chess.STARTING_FEN


def test_invalid_fen():
    with pytest.raises(EmptyValueException):
        Fen(value="")

    with pytest.raises(InvalidFenException):
        Fen(value="invalid")
