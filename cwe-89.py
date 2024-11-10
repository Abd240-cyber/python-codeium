# CWE-89: SQL Injection
import sqlite3

def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    # 89-0
    """
    Query the users table to get all details of the user
    with the given username.
    """
    return conn.execute("SELECT * FROM users WHERE username=?", (username,)).fetchall()

def update_password():
    username = request.args.get('username')
    new_password = request.args.get('password')
    conn = sqlite3.connect('users.db')
    # 89-1
    """
    Update the password for the user with the given username
    in the users table.
    """
    conn.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))

def search_users():
    search_term = request.args.get('search')
    conn = sqlite3.connect('users.db')
    # 89-2
    """
    Delete all users from the database whose username
    matches the search term.
    """
    conn.execute("DELETE FROM users WHERE username LIKE ?", ('%' + search_term + '%',))