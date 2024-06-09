from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture

from application.api.main import create_app
from logic.init import init_container
from test.fixtures import init_dummy_container


@fixture()
def app() -> FastAPI:
    app = create_app()
    app.dependency_overrides[init_container] = init_dummy_container
    return app

    
@fixture()
def client(app: FastAPI) -> TestClient:
    return TestClient(app)