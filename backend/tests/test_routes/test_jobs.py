import json


def test_create_job(client):
    data = {"title": "SDE 1 YAHOO",
            "company": "yahoo", "company_url": "yahoo.com",
            "location": "us", "description": "ygghgh", "date_posted": "2022-07-20"}
    response = client.post("/jobs/create-job", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["title"] == "SDE 1 YAHOO"
    
