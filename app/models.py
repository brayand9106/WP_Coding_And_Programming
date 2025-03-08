from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    transactions = db.relationship('Transactions', backref='users', lazy=True)

class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    income = db.Column(db.Float, nullable=False)
    expense = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Transaction {self.id}>'