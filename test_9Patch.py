from urllib import response
import requests
import pytest
import json
from jsonpath import jsonpath

def test_Patch():
    url = 'https://reqres.in/api/users/2'
    query = {
    'name':'marphues',
    'job' : 'zion resident',
        }
    response = requests.patch(url,params=query)
    Code = response.status_code
    assert Code == 200