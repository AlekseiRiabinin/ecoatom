import pytest
from redis_dict import RedisDict
from fastapi.testclient import TestClient
from models.products import X, Source, Storage
from main import app


client = TestClient(app)


@pytest.fixture(scope="function")
def redis_client():
    client = RedisDict(host="localhost", port=6379, db=0)
    yield client
    client.clear()


@pytest.fixture
def source() -> Source:
    return Source(
        name="source1",
        plastic=100,
        glass=50,
        biowaste=70
    )


@pytest.fixture
def storage() -> Storage:
    return Storage(
        name="storage1",
        max_plastic=25,
        max_glass=10,
        max_biowaste=0,
        plastic=20,
        glass=10,
        biowaste=0,
    )


@pytest.fixture
def x() -> X:
    return X(key="x", val=1000)
