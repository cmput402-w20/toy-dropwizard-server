import requests
import pytest # have to install via command "pip3 install -U pytest"

def test_health_check():
    r = requests.get('http://localhost:8085')
    assert(r.status_code == 404)

def test_id_increment():
    r = requests.get('http://localhost:8085/hello-world')
    first_id = r.json()['id']
    r = requests.get('http://localhost:8085/hello-world')
    second_id = r.json()['id']
    assert(second_id == first_id+1)

def test_stranger_name():
    r = requests.get('http://localhost:8085/hello-world')
    content = r.json()['content']
    assert(content == 'Hello, Stranger!')