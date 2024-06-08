from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass
class IllegalMoveException(LogicException):
    move: str

    @property
    def message(self):
        return f"Invalid move {self.move}"
