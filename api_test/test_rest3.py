import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_api3_getting_resource_request():
    res = requests.get(BASE_URL + "/1").json()
    assert res['id'] == 1


def test_api3_creating_resource_request():
    new_data = {
    "userID": 222,
    "id": 101,
    "title": "qwe",
    "body": "ewq"
    }
    res = requests.post(BASE_URL, json=new_data).json()
    assert res['title'] == "qwe"
    assert res['userID'] == 222
    assert res['id'] == 101
    assert res['body'] == "ewq"


@pytest.mark.parametrize('userID, id, title, body',
                         [(3, 2, 'new 1', 'new 1'),
                          (2, 2, '22', '2222'),
                          (22, 2, 'last title', 'last body')])
def test_api3_updating_resource_request(userID, id, title, body):
    new_data = {
    "userID": userID,
    "id": id,
    "title": title,
    "body": body
    }
    res = requests.put(BASE_URL + '/2', json=new_data).json()
    assert res['title'] == title
    assert res['userID'] == userID
    assert res['id'] == 2
    assert res['body'] == body


def test_api3_deleting_resource_request():
    res = requests.delete(BASE_URL + '/1')
    assert res.status_code == 200


@pytest.mark.parametrize('key, value',
                         [('userId', 1),
                          ('userId', 5),
                          ('id', 55),
                          ('id', 22)])
def test_api3_filtering_resource_request(key, value):
    res = requests.get(BASE_URL + '?', params={key:value}).json()
    for i in res:
        assert i[key] == value
    