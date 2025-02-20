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

def save_transaction(user, title, income, expense, date):
    user_id = get_user_id(user)
    if user_id is None:
        print(f"Failed to get user ID for user: {user}")
        return None
    transaction_data = {
        "user_id": user_id,
        "title": title,
        "income": income,
        "expense": expense,
        "date": date
    }
    response = requests.post(f"{BASE_URL}/transactions", json=transaction_data)
    if response.status_code != 201:
        print(f"Failed to save transaction. Response: {response.text}")
    return response.status_code

def load_transactions(user):
    user_id = get_user_id(user)
    response = requests.get(f"{BASE_URL}/transactions/{user_id}")
    if response.status_code == 200:
        try:
            transactions = response.json()
            return {i+1: {0: t['id'], 1: t['title'], 2: t['income'], 3: t['expense'], 4: t['date']} for i, t in enumerate(transactions)}
        except requests.exceptions.JSONDecodeError:
            return {}
    return {}