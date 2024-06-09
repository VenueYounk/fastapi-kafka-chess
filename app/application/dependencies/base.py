from fastapi import Depends
from punq import Container

from logic.init import init_container
from logic.mediator import Mediator

def get_mediator(container: Container = Depends(init_container)) -> Mediator:
    return container.resolve(Mediator)