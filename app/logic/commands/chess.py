from dataclasses import dataclass, field

from chess import Board

from domain.entities.chess import Game
from infrastructure.repositories.chess.base import BaseGamesRepository
from logic.commands.base import BaseCommand, CommandHandler


@dataclass(frozen=True)
class CreateGameCommand(BaseCommand):
    fen: str = field(default_factory=lambda:Board().fen())


@dataclass(frozen=True)
class CreateGameCommandHandler(CommandHandler[CreateGameCommand, Game]):
    games_repository: BaseGamesRepository

    async def handle(self, command: CreateGameCommand) -> Game:
        game = Game.create_game(command.fen)
        await self.games_repository.create(game)

        return game