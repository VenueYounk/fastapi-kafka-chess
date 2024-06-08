from dataclasses import dataclass, field

from domain.entities.base import BaseEntity
from domain.values.chess import Fen, Move
from ordered_set import OrderedSet

@dataclass(eq=False,kw_only=True)
class Game(BaseEntity):
    fen: Fen
    moves: OrderedSet[Move] = field(default_factory=OrderedSet)

    @classmethod
    def create_game(cls, fen: str) -> "Game":
        return cls(fen=Fen(fen))