from dataclasses import dataclass

from domain.exceptions.base import EmptyValueException
from domain.exceptions.chess import InvalidFenException, InvalidMoveException
from domain.values.base import BaseValueObject
import chess


@dataclass(frozen=True)
class Move(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyValueException()
        try:
            chess.Move.from_uci(self.value)
        except chess.InvalidMoveError:
            raise InvalidMoveException(move=self.value)

    def as_generic_type(self) -> str:
        return self.value
    
@dataclass(frozen=True)
class Fen(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyValueException()
        try:
            chess.Board(self.value)
        except ValueError:
            raise InvalidFenException(fen=self.value)
    
    def as_generic_type(self) -> str:
        return self.value