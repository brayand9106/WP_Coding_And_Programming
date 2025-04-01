from app import db

'''This file contains the database models for the Users and Transactions used by SQLite.'''


"""This class creates the database model for the Users table"""
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    transactions = db.relationship('Transactions', backref='users', lazy=True)

"""This class creates the database model for the Transactions table"""
class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    income = db.Column(db.Float, nullable=False)
    expense = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(120), nullable=False)

    """This method returns the transaction ID from each iteration of transaction to model"""
    def __repr__(self):
        return f'<Transaction {self.id}>'