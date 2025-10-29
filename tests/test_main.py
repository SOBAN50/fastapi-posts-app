from httpx import AsyncClient
from main import app
import pytest

@pytest.mark.asyncio
async def test_root():
    """
    Basic test for the root endpoint.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
