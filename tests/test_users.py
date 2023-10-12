import os; import sys
current = os.path.dirname(os.path.realpath(__file__)); parent = os.path.dirname(current); sys.path.append(parent)

from fastapi import testclient
from main import app

client = testclient.TestClient(app)

# def test_create_user():
