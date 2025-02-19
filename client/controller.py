import requests

BASE_URL = "http://127.0.0.1:5000/api"

def check_user_exists(username):
    response = requests.get(f"{BASE_URL}/users/{username}")
    return response.status_code == 200

def create_user(username, password):
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(f"{BASE_URL}/users", json=data)
    return response.status_code == 201

def verify_user(username, password):
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(f"{BASE_URL}/users/verify", json=data)
    return response.status_code == 200

def get_user_id(username):
    response = requests.get(f"{BASE_URL}/users/id/{username}")
    if response.status_code == 200:
        return response.json()['user_id']
    return None

def save_transactions(user, data):
    user_id = get_user_id(user)
    for transaction in data.values():
        transaction_data = {
            "user_id": user_id,
            "title": transaction[1],
            "amount": transaction[2],
            "date": transaction[4]
        }
        requests.post(f"{BASE_URL}/transactions", json=transaction_data)

def load_transactions(user):
    user_id = get_user_id(user)
    response = requests.get(f"{BASE_URL}/transactions/{user_id}")
    if response.status_code == 200:
        try:
            transactions = response.json()
            return {i+1: {0: t['id'], 1: t['title'], 2: t['amount'], 3: t['amount'], 4: t['date']} for i, t in enumerate(transactions)}
        except requests.exceptions.JSONDecodeError:
            return {}
    return {}