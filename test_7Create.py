from urllib import response
import requests
import pytest
import json
from jsonpath import jsonpath

def test_Create():
    url = 'https://reqres.in/api/users'
    query = {
    'name':'marphues',
    'job' : 'leader'
        }
    response = requests.post(url,params=query)
    Code = response.status_code
    assert Code == 201