from fastapi import Depends
from fastapi.testclient import TestClient
from main import app
from dependencies import get_current_user

client = TestClient(app)


def test_get_requests():
    response = client.get("/api/v1/requests/")
    assert response.status_code == 200
    requests = response.json()
    assert requests[0]['PartitionKey'] == 'test1@test.com'
    assert requests[0]['RowKey'] == '1'
    assert requests[1]['PartitionKey'] == 'test1@test.com'
    assert requests[1]['RowKey'] == '2'


def test_get_request1():
    response = client.get("/api/v1/requests/1")
    assert response.status_code == 200
    request = response.json()
    assert request['PartitionKey'] == 'test1@test.com'
    assert request['RowKey'] == '1'


def test_get_request1():
    response = client.get("/api/v1/requests/3")
    assert response.status_code == 200
    request = response.json()
    assert request['PartitionKey'] == 'test2@test.com'
    assert request['RowKey'] == '3'
