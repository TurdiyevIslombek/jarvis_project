import pytest
from jarvis_app.storage import save_memory, load_memory

def test_load_missing(tmp_path):
    path = tmp_path / 'nope.json'
    assert load_memory(path) == {}

def test_save_then_load(tmp_path):
    path = tmp_path / 'load.json'
    data = {"Ali": {"runs": 3}}
    save_memory(path, data)
    assert load_memory(path) == data

def test_load_broken(tmp_path):
    path = tmp_path / 'broken.json'
    with open(path, 'w', encoding='utf-8') as f:
        f.write('oops')

    assert load_memory(path) == {}