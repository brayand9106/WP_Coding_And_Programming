from flask import request, jsonify
from app import app, db
from app.models import User, Transaction

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/api/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    new_transaction = Transaction(user_id=data['user_id'], title=data['title'], amount=data['amount'], date=data['date'])
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction created successfully'}), 201

@app.route('/api/transactions/<int:user_id>', methods=['GET'])
def get_transactions(user_id):
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': t.id,
        'title': t.title,
        'amount': t.amount,
        'date': t.date
    } for t in transactions])