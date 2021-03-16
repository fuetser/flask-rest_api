import pytest
import requests


users_url = "http://localhost:5000/api/v2/users"


def test_valid_get_request():
    resp = requests.get(users_url)
    if resp.ok:
        assert resp.json().get("users") is not None, "Wrong responce"


def test_invalid_get_request():
    resp = requests.get(f"{users_url}/0")
    if resp.ok:
        assert resp.json().get("error") == "User 0 not found", "Wrong responce"


def test_adding_user():
    resp = requests.post(users_url, json={
        "id": 8,
        "surname": "Ivanov",
        "name": "Ivan",
        "age": 23,
        "position": "pilot",
        "speciality": "mechanic",
        "address": "module_2",
        "email": "ivanov1@mars.com",
        "password": "ivanov1998",
        "city_from": "Cherepovets"
    })
    if resp.ok:
        assert resp.json().get("success") is not None, "Wrong responce"


def test_empty_post_request():
    resp = requests.post(users_url)
    if resp.ok:
        assert resp.json().get("error") == "Empty request", "Wrong responce"


def test_valid_delete_request():
    resp = requests.delete(f"{users_url}/5")
    if resp.ok:
        assert resp.json().get("success") is not None, "Wrong responce"


def test_invalid_delete_request():
    resp = requests.delete(f"{users_url}/0")
    if resp.ok:
        assert resp.json().get("error") == "User 0 not found", "Wrong responce"


if __name__ == '__main__':
    pytest.main([__file__])
