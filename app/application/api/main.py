from fastapi import FastAPI
from application.api.chess.handlers import router as chess_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Chess DDD Backend",
        docs_url="/api/docs",
        description="An application that implements the chess game in DDD with FastAPI and MongoDB",
        debug=True,
    )

    app.include_router(chess_router)

    return app