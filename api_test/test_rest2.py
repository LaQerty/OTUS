import pytest
import requests

BASE_URL = "https://api.openbrewerydb.org/v1/breweries"

def test_api2_single_brewery_request():
    res = requests.get(
          BASE_URL + "/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0")
    res_json = res.json()
    assert res_json['id'] == "b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"
    assert len(res_json) == 16


@pytest.mark.parametrize('key, value',
                         [('by_city', 'Moscow'),
                          ('by_name', 'nine'),
                          ('by_type', 'bar')])
def test_api2_list_breweries_request(key, value):
    res = requests.get(BASE_URL + f'?{key}={value}')
    res_json = res.json()
    for i in res_json:
        if key == 'by_city':
            assert i['city'] == value
        if key == 'by_name':
            assert value in i['name'].lower()
        if key == 'by_type':
            assert i['brewery_type'] == value


@pytest.mark.parametrize('size', [50, 3, 12, 1, 11])
def test_api2_random_brewery_request(size):
    res = requests.get(BASE_URL + f'/random?size={size}')
    res_json = res.json()
    assert len(res_json) == size


@pytest.mark.parametrize('size, value',
                         [(3, 'rabbit'),
                          (2, 'nine'),
                          (5, 'lost')])
def test_api2_search_breweries_request(size, value):
    query = {'query': value,
         'per_page': size}
    res = requests.get(BASE_URL + '/search?', params=query)
    res_json = res.json()
    assert len(res_json) == size
    for i in res_json:
        assert value in i['name'].lower()


def test_api2_autocomplete_request():
    query = {'query': 'dog'}
    res = requests.get(BASE_URL + '/autocomplete?', params=query)
    res_json = res.json()
    for i in res_json:
        assert 'dog' in i['name'].lower()