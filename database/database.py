import os
import sqlite3

class Database:
    def __init__(self, db_name):
        script_dir = os.path.dirname(__file__)  # Get the directory of the current script
        db_path = os.path.join(script_dir, db_name)  # Construct the path to the database file
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
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
                income REAL,
                expense REAL,
                date TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        self.conn.commit()

    def insert_user(self, username, password):
        self.cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.conn.commit()

    def insert_transaction(self, user_id, title, income, expense, date):
        self.cur.execute("INSERT INTO transactions (user_id, title, income, expense, date) VALUES (?, ?, ?, ?, ?)", (user_id, title, income, expense, date))
        self.conn.commit()

    def view_users(self):
        self.cur.execute("SELECT * FROM users")
        return self.cur.fetchall()

    def view_transactions(self, user_id):
        self.cur.execute("SELECT * FROM transactions WHERE user_id=?", (user_id,))
        return self.cur.fetchall()

    def search_transactions(self, user_id, title="", income=None, expense=None, date=""):
        query = "SELECT * FROM transactions WHERE user_id=?"
        params = [user_id]
        if title:
            query += " AND title LIKE ?"
            params.append(f"%{title}%")
        if income is not None:
            query += " AND income=?"
            params.append(income)
        if expense is not None:
            query += " AND expense=?"
            params.append(expense)
        if date:
            query += " AND date LIKE ?"
            params.append(f"%{date}%")
        self.cur.execute(query, params)
        return self.cur.fetchall()

    def delete_transaction(self, id):
        self.cur.execute("DELETE FROM transactions WHERE id=?", (id,))
        self.conn.commit()

    def update_transaction(self, id, title, income, expense, date):
        self.cur.execute("UPDATE transactions SET title=?, income=?, expense=?, date=? WHERE id=?", (title, income, expense, date, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    db = Database("database.db")
    db.create_tables()