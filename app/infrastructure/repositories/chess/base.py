from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.entities.chess import Game


@dataclass
class BaseGamesRepository(ABC):
    @abstractmethod
    async def get(self, oid: str) -> Game:
        ...

    @abstractmethod
    async def create(self, game: Game):
        ...
        
    @abstractmethod
    async def update(self, game: Game):
        ...

    @abstractmethod
    async def delete(self, oid: str):
        ...

    @abstractmethod
    async def get_all(self) -> list[Game]:
        ...

    @abstractmethod
    async def exists(self, oid: str) -> bool:
        ...