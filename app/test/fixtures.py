from punq import Container, Scope
from infrastructure.repositories.chess.base import BaseGamesRepository
from infrastructure.repositories.chess.memory import MemoryGamesRepository
from logic.init import _init_container


def init_dummy_container() -> Container:
    container = _init_container()

    container.register(BaseGamesRepository, MemoryGamesRepository, scope=Scope.singleton)
    return container