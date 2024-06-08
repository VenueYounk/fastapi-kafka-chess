from dataclasses import dataclass
from motor.core import AgnosticClient


@dataclass
class BaseMongoDBRepository:
    client: AgnosticClient
    db_name: str
    collection_name: str

    @property
    def _collection(self):
        return self.client[self.db_name][self.collection_name]