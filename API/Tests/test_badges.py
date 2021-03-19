from fastapi import Depends
from fastapi.testclient import TestClient
from main import app
from dependencies import get_current_user

client = TestClient(app)


async def override():
    return None

app.dependency_overrides[get_current_user] = override


def test_get_badges():
    response = client.get("/api/v1/badges/")
    assert response.status_code == 200
    badges = response.json()
    assert badges[0]['PartitionKey'] == 'Milestone'
    assert badges[0]['RowKey'] == '1'
    assert badges[1]['PartitionKey'] == 'Milestone'
    assert badges[1]['RowKey'] == '2'


def test_get_badge1():
    response = client.get("/api/v1/badges/1")
    assert response.status_code == 200
    badge = response.json()
    assert badge['PartitionKey'] == 'Milestone'
    assert badge['RowKey'] == '1'


def test_get_badge2():
    response = client.get("/api/v1/badges/2")
    assert response.status_code == 200
    badge = response.json()
    assert badge['PartitionKey'] == 'Milestone'
    assert badge['RowKey'] == '2'

# TODO: Badge post request

# TODO: Badge put request
