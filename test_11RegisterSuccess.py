from urllib import response
import requests
import pytest
import json
from os import read
from jsonpath import jsonpath

def test_RegisterSuccess():
    url = 'https://reqres.in/api/register'
    file = open('E:\BELAJARQA\API AUTOMATION\Register.json','r')
    #changes with file address on your computer
    request_json = json.loads(file.read())
    response = requests.post(url,json=request_json)
    Code = response.status_code

    assert Code == 200
