from ast import List
import requests
import pytest
import json
from jsonpath import jsonpath

def test_get_user():
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    Code = response.status_code
    assert Code == 200
  
   