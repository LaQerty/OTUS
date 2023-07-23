import pytest
import requests

def test_addoption(url, status_code):
    res = requests.get(url)
    assert res.status_code == int(status_code)