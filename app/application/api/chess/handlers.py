from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter

from application.api.chess.schemas import CreateGameRequest, CreateGameResponse
from application.dependencies.base import get_mediator
from domain.exceptions.base import ApplicationException
from logic.commands.chess import CreateGameCommand
from logic.mediator import Mediator

router = APIRouter(prefix="/chess", tags=["Chess"])


@router.post("/create",
             response_model=CreateGameResponse,
             status_code=status.HTTP_201_CREATED,
             description="Creates a new game.")
async def create_game(schema: CreateGameRequest,
                 mediator: Mediator = Depends(get_mediator)):
    """
    Creates a new game with the given FEN position or with the default position."""
    try:
        game, *_ = await mediator.handle_command(
            CreateGameCommand(fen=schema.fen))
    except ApplicationException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={"error": e.message})

    return CreateGameResponse.from_entity(game)
