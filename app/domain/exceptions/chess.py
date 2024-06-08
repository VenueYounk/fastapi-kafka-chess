

from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass
class InvalidMoveException(ApplicationException):
    move: str

    @property
    def message(self):
        return f"Invalid move: {self.move}"

@dataclass
class InvalidFenException(ApplicationException):
    fen: str

    @property
    def message(self):
        return f"Invalid fen: {self.fen}"