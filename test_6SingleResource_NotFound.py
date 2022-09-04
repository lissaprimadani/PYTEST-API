from urllib import response
import requests
import pytest
import json
from jsonpath import jsonpath

def test_Single_Resource_Not_Found():
    url = 'https://reqres.in/api/unknown/23'
    response = requests.get(url)
    Code = response.status_code
    json_response = json.loads(response.text)

    assert Code == 404
    assert json_response == {}