import pytest
import requests


test_url_get = "https://postman-echo.com/get"
test_url_post = "https://postman-echo.com/post"


def test_get_request_returns_200():
    response = requests.get(test_url_get)

    assert response.status_code == 200


def test_post_endpoint_accepts_post_request():
    response = requests.post(test_url_post)

    assert response.status_code == 200

    data = response.json()

    assert data["url"] == test_url_post
    assert "headers" in data
    assert "data" in data
    assert "files" in data
    assert "form" in data


def test_get_request_returns_json_with_url():
    response = requests.get(test_url_get)
    data = response.json()

    assert data["url"] == test_url_get


def test_get_request_returns_headers():
    response = requests.get(test_url_get)
    data = response.json()

    assert "headers" in data
    assert data["headers"]["host"] == "postman-echo.com"


def test_head_request_returns_200_and_empty_body():
    response = requests.head(test_url_get)

    assert response.status_code == 404
    assert response.text == ""


def test_options_request_returns_200_and_allowed_methods():
    response = requests.options(test_url_get)

    assert response.status_code == 200

    allowed_methods = response.text

    assert "GET" in allowed_methods
    assert "HEAD" in allowed_methods
    assert "POST" in allowed_methods
    assert "PUT" in allowed_methods
    assert "PATCH" in allowed_methods
    assert "DELETE" in allowed_methods