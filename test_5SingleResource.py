from codecs import Codec
from urllib import response
import requests
import pytest
import json
from jsonpath import jsonpath

def test_get_SingleResource():
    url = 'https://reqres.in/api/unknown/2'
    response = requests.get(url)
    Code = response.status_code
    json_response = json.loads(response.text)
    NM = jsonpath(json_response['data'],'name')
    
    assert Code == 200 
    assert NM[0] == 'fuchsia rose'