from typing import Mapping

from domain.entities.chess import Game


def from_game_entity_to_dict(game: Game) -> dict:
    return {"oid" : str(game.oid), "fen" : game.fen.as_generic_type(), "moves" : list(game.moves)}
