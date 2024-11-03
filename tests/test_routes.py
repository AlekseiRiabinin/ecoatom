import pytest
from httpx import AsyncClient, ASGITransport
from main import app


@pytest.mark.anyio
async def test_get_database(redis_client) -> None:
    transport = ASGITransport(app=app)
    client = AsyncClient(transport=transport)
    response = await client.get("http://localhost:8000/database/")
    assert response.status_code == 200
    assert response.json() == {}


@pytest.mark.anyio
async def test_post_x(redis_client) -> None:
    transport = ASGITransport(app=app)
    client = AsyncClient(transport=transport)

    payload = {"key": "x", "val": 1000}
    headers = {"Content-Type": "application/json"}
    success_response = {"message": "X created successfully"}

    response = await client.post(
        "http://localhost:8000/x/",
        json=payload,
        headers=headers
    )

    assert response.status_code == 200
    assert response.json() == success_response


@pytest.mark.anyio
async def test_post_source(redis_client) -> None:
    transport = ASGITransport(app=app)
    client = AsyncClient(transport=transport)

    payload = [
        {"name": "source1", "plastic": 100, "glass": 50, "biowaste": 70}
    ]

    headers = {"Content-Type": "application/json"}
    success_response = {"message": "Source created successfully"}

    response = await client.post(
        "http://localhost:8000/source/",
        json=payload,
        headers=headers
    )

    assert response.status_code == 200
    assert response.json() == success_response
