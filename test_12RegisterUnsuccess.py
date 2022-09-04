from urllib import response
import requests
import pytest
import json
from jsonpath import jsonpath

def test_RegisterUnsuccess():
    url = 'https://reqres.in/api/register'
    query = {
    'email':'eve.holt@reqres.in',
    'password' : ''
        }
    response = requests.post(url,params=query)
    Code = response.status_code
    assert Code == 400