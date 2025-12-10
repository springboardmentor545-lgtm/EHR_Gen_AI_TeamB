import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

def signup(username, password):
    try:
        resp = requests.post(f"{API_URL}/signup", json={
            "username": username,
            "password": password
        })
        if resp.status_code == 200:
            return True, resp.json()
        return False, resp.json()
    except Exception as e:
        return False, {"error": str(e)}

def login(username, password):
    try:
        resp = requests.post(f"{API_URL}/login", json={
            "username": username,
            "password": password
        })
        if resp.status_code == 200:
            return True, resp.json()
        return False, resp.json()
    except Exception as e:
        return False, {"error": str(e)}
