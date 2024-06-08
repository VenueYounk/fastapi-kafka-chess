from functools import lru_cache

from infrastructure.repositories.chess.base import BaseGamesRepository
from infrastructure.repositories.chess.mongo import MongoDBGamesRepository
from logic.commands.chess import CreateGameCommand, CreateGameCommandHandler
from logic.mediator import Mediator
from motor.motor_asyncio import AsyncIOMotorClient
from punq import Container, Scope
from settings import Config


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    container.register(Config, instance=Config(), scope=Scope.singleton)

    container.register(CreateGameCommandHandler)


    def init_mediator():
        mediator = Mediator()

        mediator.register_command(
            CreateGameCommand,
            [container.resolve(CreateGameCommandHandler)],
        )

        return mediator

    container.register(Mediator, factory=init_mediator)
    
    def init_mongo_db_games_repository():
        config: Config = container.resolve(Config)
        client = AsyncIOMotorClient(
            config.mongodb_uri, serverSelectionTimeoutMS=5000
        )
        return MongoDBGamesRepository(
            client=client,
            db_name=config.mongodb_chess_db_name,
            collection_name=config.mongodb_chess_collection_name,
        )

    container.register(BaseGamesRepository, factory=init_mongo_db_games_repository, scope=Scope.singleton)

    return container

