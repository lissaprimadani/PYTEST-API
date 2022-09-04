from urllib import response
import requests
import pytest
import json
from jsonpath import jsonpath

def test_Delete():
    url = 'https://reqres.in/api/users/2'
    response = requests.delete(url)
    Code = response.status_code
    assert Code == 204