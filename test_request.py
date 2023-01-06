import requests
from typing import Dict
import json

headers = {'Content-Type': 'application/x-www-form-urlencoded'}


def post_request(data:Dict):
    resp = requests.post('http://127.0.0.1:5000/get_form', headers=headers, data=data)
    return resp.text


def test_template1():
    assert post_request({'email': 'a@gmail.com', 'text': 'abc', 'phone': '+7 000 000 00 00', 'date': '12.02.2000'}) == 'template1'


def test_template2():
    assert post_request({'work_email': 'a@gmail.com', 'work_phone': '+7 000 000 00 00'}) == 'template2'


def test_template1_more_fields():
    assert post_request({'email': 'a@gmail.com', 'text': 'abc', 'phone': '+7 000 000 00 00', 'date': '12.02.2000',
                         'data': 'abcd', 'greeting': 'hello'}) == 'template1'


def test_template1_wrong_types():
    assert json.loads(post_request({'email': 'gmail.com', 'text': '05.05.2005', 'phone': 'email@gmail.com', 'date': '12022000'})) \
           == {'email': 'text', 'text': 'date', 'phone': 'email', 'date': 'text'}


def test_no_matches():
    assert json.loads(post_request({'document': 'contract', 'start_day': '05.05.2005', 'contact': 'email@gmail.com', 'description': 'lorem_ipsum'})) \
           == {'document': 'text', 'start_day': 'date', 'contact': 'email', 'description': 'text'}
