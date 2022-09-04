from codecs import Codec
from urllib import response
import requests
import pytest
import json
from jsonpath import jsonpath

def test_List_Resource():
    url = 'https://reqres.in/api/unknown'
    response = requests.get(url)
    Code = response.status_code
    assert Code == 200
    
