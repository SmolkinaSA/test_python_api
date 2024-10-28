import requests

def test_api_status():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    return response

def test_api_content():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert len(response.json()) > 0