from urllib import response
import requests
import pytest
import json
from jsonpath import jsonpath

def test_LoginUnsuccess():
    url = 'https://reqres.in/api/login'
    query = {
    'email':'email": "peter@klaven'
        }
    response = requests.post(url,params=query)
    Code = response.status_code
    assert Code == 400