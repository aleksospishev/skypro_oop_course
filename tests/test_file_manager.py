from src.file_manager import JsonFileManager
import json
import os

test_saver = JsonFileManager("./data_test/test.json")


def test_write_data(data_file_manager):
    test_saver.write_data(data_file_manager)
    with open("./data_test/test.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data[0]["name"] == "Strong Junior Backend разработчик"
    assert data[1]["name"] == "Backend-разработчик"


def test_load_reader():
    data = test_saver.load_data()
    assert data[0].name == "Strong Junior Backend разработчик"
    assert data[0].area["name"] == "Алматы"
    assert data[0].salary_from == 250000
    assert data[1].name == "Backend-разработчик"


def test_delete_data():
    test_saver.delete_data()
    assert os.stat("./data_test/test.json").st_size == 0
