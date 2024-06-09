from dataclasses import field
import datetime
from chess import STARTING_FEN
from pydantic import BaseModel

from domain.entities.chess import Game


class CreateGameRequest(BaseModel):
    fen: str = field(default=STARTING_FEN)


class CreateGameResponse(BaseModel):
    game_id: str
    game_fen: str

    @classmethod
    def from_entity(cls, game: Game):
        return cls(game_id=str(game.oid), game_fen=game.fen.as_generic_type())