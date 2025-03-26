import requests
import json

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
    return response

def load_transactions(user):
    user_id = get_user_id(user)
    response = requests.get(f"{BASE_URL}/transactions/{user_id}")
    if response.status_code == 200:
        try:
            transactions = response.json()
            return [
                {
                    "id": t['id'],
                    "title": t['title'],
                    "income": t['income'],
                    "expenses": t['expense'],
                    "date": t['date']
                }
                for t in transactions
            ]
        except requests.exceptions.JSONDecodeError:
            return []
    return []

def delete_transaction(transaction_id):
    response = requests.delete(f"{BASE_URL}/transactions/{transaction_id}")
    return response.status_code == 200

def get_chatbot_response(user_input, stream=False):
    data = {
        "input": user_input
    }
    headers = {
        "Accept": "application/json"
    }
    try:
        response = requests.post(f"{BASE_URL}/chatbot", json=data, headers=headers)
        response.raise_for_status()

        if stream:
            for line in response.iter_lines(decode_unicode=True):
                if line:
                    yield json.loads(line)
        else:
                return response.json()['response']
    except requests.exceptions.RequestException as e:
        print(f"RequestException: {str(e)}")
        yield {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        yield {"error": f"Unexpected error: {str(e)}"}
    '''
    response = requests.post(f"{BASE_URL}/chatbot", json=data)
    if response.status_code == 200:
        return response.json()['response']
    return "Error processing request"'
    '''