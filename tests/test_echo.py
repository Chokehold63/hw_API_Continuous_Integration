import requests


test_url = "https://postman-echo.com/get"


def test_get_request_returns_200():
    response = requests.get(test_url)

    assert response.status_code == 200


def test_get_request_returns_json_with_url():
    response = requests.get(test_url)
    data = response.json()

    assert data["url"] == test_url


def test_get_request_returns_headers():
    response = requests.get(test_url)
    data = response.json()

    assert "headers" in data
    assert "host" in data["headers"]
    assert data["headers"]["host"] == "postman-echo.com"


def test_post_request_to_get_endpoint_returns_404():
    response = requests.post(test_url)

    assert response.status_code == 404


def test_put_request_to_get_endpoint_returns_404():
    response = requests.put(test_url)

    assert response.status_code == 404


def test_patch_request_to_get_endpoint_returns_404():
    response = requests.patch(test_url)

    assert response.status_code == 404


def test_delete_request_to_get_endpoint_returns_404():
    response = requests.delete(test_url)

    assert response.status_code == 404


def test_head_request_returns_200_and_empty_body():
    response = requests.head(test_url)

    assert response.status_code == 200
    assert response.text == ""


def test_options_request_returns_200_and_allowed_methods():
    response = requests.options(test_url)

    assert response.status_code == 200

    allowed_methods = response.text

    assert "GET" in allowed_methods
    assert "HEAD" in allowed_methods
    assert "POST" in allowed_methods
    assert "PUT" in allowed_methods
    assert "PATCH" in allowed_methods
    assert "DELETE" in allowed_methods