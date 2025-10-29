import sys
import os
import pytest

# Ensure repo root is in the import path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Settings

@pytest.fixture(autouse=True)
def patch_settings(monkeypatch):
    monkeypatch.setenv("database_username", "postgres")
    monkeypatch.setenv("database_password", "postgres")
    monkeypatch.setenv("database_hostname", "localhost")
    monkeypatch.setenv("database_port", "5432")
    monkeypatch.setenv("database_name", "test_db")
    monkeypatch.setenv("secret_key", "testkey")
    monkeypatch.setenv("algorithm", "HS256")
    monkeypatch.setenv("access_token_expire_minutes", "30")
