import chess
import pytest

from domain.entities.chess import Game
from infrastructure.repositories.chess.base import BaseGamesRepository
from logic.commands.chess import CreateGameCommand
from logic.mediator import Mediator


@pytest.mark.asyncio
async def test_create_game_command_success(games_repository: BaseGamesRepository, mediator: Mediator):
    created_game, *_ = await mediator.handle_command(CreateGameCommand(fen=chess.STARTING_BOARD_FEN))
    created_game: Game

    assert created_game
    assert await games_repository.exists(str(created_game.oid))