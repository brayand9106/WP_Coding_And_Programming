import sqlite3
import os

class Database:
    def __init__(self, db_name):
        script_dir = os.path.dirname(__file__)  # Get the directory of the current script
        db_path = os.path.join(script_dir, db_name)  # Construct the path to the database file
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT
            )
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                title TEXT,
                amount REAL,
                date TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        self.conn.commit()

    def insert_user(self, username, password):
        self.cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.conn.commit()

    def insert_transaction(self, user_id, title, amount, date):
        self.cur.execute("INSERT INTO transactions (user_id, title, amount, date) VALUES (?, ?, ?, ?)", (user_id, title, amount, date))
        self.conn.commit()

    def view_users(self):
        self.cur.execute("SELECT * FROM users")
        rows = self.cur.fetchall()
        return rows

    def view_transactions(self, user_id):
        self.cur.execute("SELECT * FROM transactions WHERE user_id=?", (user_id,))
        rows = self.cur.fetchall()
        return rows

    def search_transactions(self, user_id, title="", amount=None, date=""):
        query = "SELECT * FROM transactions WHERE user_id=?"
        params = [user_id]
        if title:
            query += " AND title=?"
            params.append(title)
        if amount is not None:
            query += " AND amount=?"
            params.append(amount)
        if date:
            query += " AND date=?"
            params.append(date)
        self.cur.execute(query, tuple(params))
        rows = self.cur.fetchall()
        return rows

    def delete_transaction(self, id):
        self.cur.execute("DELETE FROM transactions WHERE id=?", (id,))
        self.conn.commit()

    def update_transaction(self, id, title, amount, date):
        self.cur.execute("UPDATE transactions SET title=?, amount=?, date=? WHERE id=?", (title, amount, date, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()