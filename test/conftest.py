from typing import Container
from pytest import fixture

from infrastructure.repositories.chess.base import BaseGamesRepository
from logic.mediator import Mediator
from test.fixtures import init_dummy_container


@fixture(scope="function")
def container() -> Container:
    return init_dummy_container()

@fixture(scope="function")
def mediator(container) -> Mediator:
    return container.resolve(Mediator)

@fixture(scope="function")
def games_repository(container) -> BaseGamesRepository:
    return container.resolve(BaseGamesRepository)