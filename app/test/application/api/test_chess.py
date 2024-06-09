from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

import chess


@pytest.mark.asyncio
async def test_create_game_success(app: FastAPI, client: TestClient):
    """Test that creating a game with a valid FEN position returns a success response."""

    url = app.url_path_for("create_game")
    response = client.post(url, json={"fen": chess.STARTING_FEN})

    assert response.is_success
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_create_game_with_invalid_fen(app: FastAPI, client: TestClient):
    """Test that creating a game with an invalid FEN position returns an error."""

    url = app.url_path_for("create_game")
    invalid_fen_response = client.post(url, json={"fen": "invalid"})

    assert invalid_fen_response.status_code == 400
    assert invalid_fen_response.json()["detail"]["error"].startswith(
        "Invalid fen: ")
