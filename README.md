# WP_Coding_And_Programming
FBLA West Point High School IT 2024-2025 Coding and Programming Repository

# 📱 Pynancial Pro

"A simple yet efficient Python productivity app that helps you plan your finances featuring AI support and Statistical Analysis"

## 📸 Screenshots

![Screenshot](https://github.com/brayand9106/WP_Coding_And_Programming/blob/main/client/Images/LogoPynancial2.png?raw=true)

## 🧰 Features (Not limited to:)

- ✅ Simple Input Responses For Your Finances
- ✅ Real Time Data Storage
- ✅ AI Support For Navigation Assistance
- ✅ Multiple Analysis Options

## 🛠️ Tech Stack (Fully Python Built!)

- **Frontend:** CustomTkinter Powered by Python
- **Backend:** Flask
- **Database:** SQLite
- **Other Tools:** Llama AI, Jsonify

## 🚀 Getting Started

### Prerequisites

- [Ollama](https://ollama.com/) *To utilize chatbot with installation of llama3.2
- [Python3.13](https://www.python.org/) *Mandatory for use
- [SQLite](https://sqlite.org/index.html) *To utilize local database (pip installed via installation)
- [Flask](https://flask.palletsprojects.com/en/stable/) *To utilize local backend (pip installed via installation)

### Installation

```bash
# Clone the repository
git clone https://github.com/brayand9106/WP_Coding_And_Programming/
cd yourproject

# Install dependencies
cmd //c Requirements.bat

# Run the app
Python start.py
```
### Ensure that database is intialized
1. Initialize the database(only once):

flask shell
>>> from app import db
>>> db.create_all()
>>> exit()

