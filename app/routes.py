from flask import request, jsonify
from app import app, db
from app.models import Users, Transactions

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = Users(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/api/users/<username>', methods=['GET'])
def check_user(username):
    user = Users.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'User exists'}), 200
    else:
        return jsonify({'message': 'User does not exist'}), 404
    
@app.route('/api/users/verify', methods=['POST'])
def verify_user():
    data = request.get_json()
    user = Users.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        return jsonify({'message': 'User verified'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
    
@app.route('/api/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    new_transaction = Transactions(user_id=data['user_id'], title=data['title'], income=data['income'], expense=data['expense'], date=data['date'])
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction created successfully'}), 201

@app.route('/api/users/id/<username>', methods=['GET'])
def get_user_id(username):
    user = Users.query.filter_by(username=username).first()
    if user:
        return jsonify({'user_id': user.id}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/api/transactions/<int:user_id>', methods=['GET'])
def get_transactions(user_id):
    transactions = Transactions.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': t.id,
        'title': t.title,
        'income': t.income,
        'expense': t.expense,
        'date': t.date
    } for t in transactions])