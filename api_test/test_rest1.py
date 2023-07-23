import pytest
import requests

BASE_URL = "https://dog.ceo/api/"

def test_api1_list_all_breeds_request():
    res = requests.get(
          BASE_URL + "breeds/list/all")
    res_json = res.json()
    assert res_json['status'] == "success"
    assert len(res_json['message']) == 98


@pytest.mark.parametrize('img_count', [50, 3, 12, 1, 11, 0])
def test_api1_random_image_request(img_count):
    if img_count > 0:
        res = requests.get(
            BASE_URL + "breeds/image/random" + f"/{img_count}")
        res_json = res.json()
        assert len(res_json['message']) == img_count
    else: 
        res = requests.get(
            BASE_URL + "breeds/image/random")
        res_json = res.json()
        assert ".jpg" in res_json['message']
    assert res_json['status'] == "success"


@pytest.mark.parametrize('breed', ['hound', 'poodle', 'akita', 'basenji'])
def test_api1_by_breed_request(breed):
    res = requests.get(
        BASE_URL + f"breed/{breed}/images/random")
    res_json = res.json()
    assert res_json['status'] == "success"
    assert f"https://images.dog.ceo/breeds/{breed}" in res_json['message']


@pytest.mark.parametrize('sub_count, breed',
                         [(7, 'hound'),
                          (4, 'poodle'),
                          (0, 'akita')])
def test_api1_list_all_sub_breed_request(breed, sub_count):
    res = requests.get(
        BASE_URL + f"breed/{breed}/list")
    res_json = res.json()
    assert res_json['status'] == "success"
    assert len(res_json['message']) == sub_count


@pytest.mark.parametrize('breed, sub_breed',
                         [('hound', 'afghan'),
                          ('poodle', 'miniature'),
                          ('pointer', 'german')])
def test_api1_list_all_sub_breed_images_request(breed, sub_breed):
    res = requests.get(
        BASE_URL + f"breed/{breed}/{sub_breed}/images")
    res_json = res.json()
    assert res_json['status'] == "success"