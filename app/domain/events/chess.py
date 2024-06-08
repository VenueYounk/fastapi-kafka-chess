from dataclasses import dataclass

from domain.entities.chess import Game
from domain.events.base import BaseEvent
from domain.values.chess import Move


@dataclass(frozen=True)
class GameEvent(BaseEvent):
    pass


@dataclass
class NewGameCreatedEvent(GameEvent):
    game: Game


@dataclass
class NewMoveEvent(GameEvent):
    move: Move
