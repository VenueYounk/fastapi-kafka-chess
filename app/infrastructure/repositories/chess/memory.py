from dataclasses import dataclass, field

from domain.entities.chess import Game
from infrastructure.repositories.chess.base import BaseGamesRepository

GameID = str

@dataclass
class MemoryGamesRepository(BaseGamesRepository):
    games: dict[GameID, Game] = field(default_factory=dict)

    async def get(self, oid: GameID) -> Game:
        return self.games[oid]
    
    async def create(self, game: Game):
        self.games[str(game.oid)] = game

    async def update(self, game: Game):
        self.games[str(game.oid)] = game

    async def delete(self, oid: GameID):
        del self.games[oid]

    async def get_all(self) -> list[Game]:
        return list(self.games.values())
    
    async def exists(self, oid: GameID) -> bool:
        return oid in self.games.keys()