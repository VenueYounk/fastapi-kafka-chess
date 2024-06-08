from pydantic_settings import BaseSettings

class Config(BaseSettings):
    mongodb_uri: str
    mongodb_chess_db_name: str
    mongodb_chess_collection_name: str
    