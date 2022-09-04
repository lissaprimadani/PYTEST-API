from urllib import response
import requests
import pytest
import json
from jsonpath import jsonpath

def test_get_user():
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    Code = response.status_code
    json_response = json.loads(response.text)
    Email = jsonpath(json_response ['data'][1], 'email')

    assert Code == 200 
    assert Email[0] == 'lindsay.ferguson@reqres.in'