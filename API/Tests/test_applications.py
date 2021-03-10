from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_applications():
    response = client.get("/api/v1/applications/")
    assert response.status_code == 200
    applications = response.json()
    assert applications[0]['PartitionKey'] == 'test1@test.com'
    assert applications[0]['RowKey'] == '1'
    assert applications[1]['PartitionKey'] == 'test2@test.com'
    assert applications[1]['RowKey'] == '2'


def test_get_application1():
    response = client.get("/api/v1/applications/1")
    assert response.status_code == 200
    application = response.json()
    assert application['PartitionKey'] == 'test1@test.com'
    assert application['RowKey'] == '1'
    badge_requests = application['requests']
    assert badge_requests[0]['PartitionKey'] == 'test1@test.com'
    assert badge_requests[0]['RowKey'] == '1'


def test_get_application2():
    response = client.get("/api/v1/applications/2")
    assert response.status_code == 200
    application = response.json()
    assert application['PartitionKey'] == 'test2@test.com'
    assert application['RowKey'] == '2'
    badge_requests = application['requests']
    assert badge_requests[0]['PartitionKey'] == 'test2@test.com'
    assert badge_requests[0]['RowKey'] == '3'


def test_post_application():
    response = client.post(
        "/api/v1/applications/",
        json={"email": "test3@test.com", "requests": [{"email": "test3@test.com", "badgeID": "1", "category": "Milestone"}, {
            "email": "test3@test.com", "badgeID": "2", "category": "Milestone"}]}
    )
    assert response.status_code == 200
    data = response.json()
    assert data == {"email": "test3@test.com", "requests": [{"email": "test3@test.com", "badgeID": "1", "category": "Milestone"}, {
        "email": "test3@test.com", "badgeID": "2", "category": "Milestone"}]}
