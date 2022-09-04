from urllib import response
import requests
import pytest
import json
from jsonpath import jsonpath

def test_DelayResponsed():
    url = 'https://reqres.in/api/users?delay=3'
    response = requests.get(url)
    Code = response.status_code
    json_response = json.loads(response.text)
    Name = jsonpath(json_response['data'][1],'first_name')

    assert Code == 200
    assert Name[0] == "Janet"