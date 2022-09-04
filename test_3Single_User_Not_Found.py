from codecs import Codec
from urllib import response
import requests
import pytest
import json
from jsonpath import jsonpath


def test_single_user_not_found():
    url = 'https://reqres.in/api/users/23'
    response = requests.get(url)
    Code = response.status_code
    json_response = json.loads(response.text)


    assert Code == 404
    assert json_response == {}