from dataclasses import dataclass
from typing import Optional

from motor.core import AgnosticClient

from domain.entities.chess import Game
from infrastructure.repositories.chess.datamappers import from_game_entity_to_dict
from infrastructure.repositories.mongo_base import BaseMongoDBRepository
from infrastructure.repositories.chess.base import BaseGamesRepository


@dataclass
class MongoDBGamesRepository(BaseGamesRepository, BaseMongoDBRepository):

    async def get(self, oid: str) -> Game:
        return await self._collection.find_one({"oid": oid})

    async def create(self, game: Game):
        await self._collection.insert_one(from_game_entity_to_dict(game))

    async def update(self, game: Game):
        await self._collection.replace_one({"oid": game.oid}, from_game_entity_to_dict(game), upsert=True)

    async def delete(self, oid: str):
        await self._collection.delete_one({"oid": oid})

    async def get_all(self) -> list[Game]:
        return await self._collection.find({}).to_list(None)
    
    async def exists(self, game_oid: str) -> bool:
        """Check if a game with the given oid exists in the repository."""
        document = await self._collection.find_one({"oid": game_oid})
        return document is not None

