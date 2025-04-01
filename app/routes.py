from flask import request, jsonify
import json
from app import app, db
from app.models import Users, Transactions

'''This file contains the routes for the Flask application, 
handling user and transaction management.'''

try:
    import ollama
    hasollama=True
except ImportError:
    print("Please install the 'ollama' package using 'pip install ollama'")
    hasollama=False

if hasollama:
    from ollama import chat, ChatResponse

"""This route handles the creation of a new user."""
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = Users(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

"""This route handles the verification of user existence"""
@app.route('/api/users/<username>', methods=['GET'])
def check_user(username):
    user = Users.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'User exists'}), 200
    else:
        return jsonify({'message': 'User does not exist'}), 404
    
"""This route handles the verification of user credentials"""
@app.route('/api/users/verify', methods=['POST'])
def verify_user():
    data = request.get_json()
    user = Users.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        return jsonify({'message': 'User verified'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
    
"""This route handles the creation of a new transaction to database."""
@app.route('/api/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    new_transaction = Transactions(
        user_id=data['user_id'],
        title=data['title'],
        income=data['income'],
        expense=data['expense'],
        date=data['date']
    )
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction created successfully', 'transaction_id': new_transaction.id}), 201

"""This route handles the deletion of transactions from database from user."""
@app.route('/api/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    transaction = Transactions.query.get(transaction_id)
    if transaction:
        db.session.delete(transaction)
        db.session.commit()
        return jsonify({'message': 'Transaction deleted successfully'}), 200
    else:
        return jsonify({'message': 'Transaction not found'}), 404

"""This route handles the requests to get user id"""
@app.route('/api/users/id/<username>', methods=['GET'])
def get_user_id(username):
    user = Users.query.filter_by(username=username).first()
    if user:
        return jsonify({'user_id': user.id}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

"""This route handles the requests to get all transactions for a user"""
@app.route('/api/transactions/<int:user_id>', methods=['GET'])
def get_transactions(user_id):
    transactions = Transactions.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': t.id,
        'title': t.title,
        'income': t.income,
        'expense': t.expense,
        'date': t.date if isinstance(t.date, str) else t.date.strftime("%m/%d/%Y")  # Ensure date is formatted as a string
    } for t in transactions])

"""This route handles the requests for chatbot responses by client"""
@app.route('/api/chatbot', methods=['POST'])
def chatbot_response():
    if not hasollama:
        return jsonify({'error': 'ollama package is not installed. Please install the package using "pip install ollama"'}), 500
    data = request.get_json()
    user_input = data['input']

    detailed_summary = (
        "You are a help chatbot for a financial management application called Pynancial Pro. Information about the application is as follows:\n\n"
        "Pynancial Pro is a comprehensive financial management application designed to help users manage their finances effectively. "
        "The application includes the following features:\n"
        "1. **User Management**: Users can create accounts, log in, and verify their credentials.\n"
        "2. **Transaction Management**: Users can create, view, and delete financial transactions. Each transaction includes details such as title, income, expense, and date.\n"
        "3. **Statistics and Reports**: The application provides graphical summaries of incomes and expenses over different time ranges (week, month, year). Users can generate graphs for income/expenses, net earnings, and cumulative earnings.\n"
        "4. **Home Dashboard**: The home display offers a summary of the user's transactions, recent updates, and a graph displaying a summary of transactions over the last week.\n"
        "5. **Help and Support**: The application includes a help section with detailed explanations of each feature and a chatbot to assist users with their questions.\n"
        "Please provide your query or question below, and I will assist you based on the information provided." \
        "(As the chatbot, its your job to answer the user's question based on the information provided in the detailed summary above. Do not ask me questions regarding needing more information from the creators.)\n\n"
    )
    combined_input = detailed_summary + "\n\nUser Query: " + user_input

    try:
        # Use ollama to generate a response
        response: ChatResponse = chat(model="llama3.2", messages=[{'role': 'user', 'content': combined_input}])
        output_text = response.message.content
        return jsonify({'response': output_text})
    except ollama.ResponseError as e:
        return jsonify({'error': str(e)}), e.status_code
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500
