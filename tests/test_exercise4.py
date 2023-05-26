import pytest
import sys
import sqlite3
from math import pi

sys.path.append(r'D:\coding\functional_test')

from exercice4 import DatabaseManager

@pytest.fixture
def database_manager():
    db_name = "test.db"
    return DatabaseManager(db_name)

def test_create_table(database_manager):
    columns = {
        "id": "INTEGER",
        "name": "TEXT",
        "age": "INTEGER"
    }
    database_manager.create_table("users", columns)

def test_insert_into_table(database_manager):
    data = {
        "id": 1,
        "name": "YOUR MOM IS GAY",
        "age": 30
    }
    database_manager.insert_into_table("users", data)

def test_select_from_table(database_manager):
    data = {
        "id": 1,
        "name": "YOUR MOM IS GAY",
        "age": 30
    }
    database_manager.insert_into_table("users", data)

    result = database_manager.select_from_table("users")

    assert len(result) == 1
    assert result[0][0] == 1
    assert result[0][1] == "YOUR MOM IS GAY"
    assert result[0][2] == 30

def test_update_table(database_manager):
    data = {
        "id": 1,
        "name": "YOUR MOM IS GAY",
        "age": 30
    }
    database_manager.insert_into_table("users", data)

    updated_data = {
        "name": "EREN YEAGER",
        "age": 35
    }
    condition = "id = 1"
    database_manager.update_table("users", updated_data, condition)

    result = database_manager.select_from_table("users")

    assert len(result) == 1
    assert result[0][0] == 1
    assert result[0][1] == "EREN YEAGER"
    assert result[0][2] == 35

def test_delete_from_table(database_manager):
    data = {
        "id": 1,
        "name": "YOUR MOM IS GAY",
        "age": 30
    }
    database_manager.insert_into_table("users", data)

    condition = "id = 1"
    database_manager.delete_from_table("users", condition)

    result = database_manager.select_from_table("users")

    assert len(result) == 0

def test_close_connection(database_manager):
    database_manager.close_connection()

