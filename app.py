from flask import Flask, render_template, request, redirect, url_for
import hashlib
import os
from flask import session
import logging

logging.basicConfig(filename='login_attempts.log', level=logging.INFO)
#"python app.py" to run

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a strong secret key

users = {}

def hash_password(password):
    # Generate a random salt
    salt = os.urandom(16).hex()
    
    # Combine the salt and password and hash them together
    hashed_password = hashlib.sha256((salt + password).encode()).hexdigest()
    
    return hashed_password, salt

def verify_password(password, stored_hash, salt):
    # Verify the entered password against the stored hash and salt
    entered_hash = hashlib.sha256((salt + password).encode()).hexdigest()
    return entered_hash == stored_hash
def is_strong_password(password):
    # Check for strong password requirements
    return len(password) >= 8 and any(char.isupper() for char in password) and \
           any(char.islower() for char in password) and any(char.isdigit() for char in password) and \
           any(char in '!@#$%^&*()-_+=[]{}|;:,.<>?/' for char in password)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if 'register' in request.form:
            if not is_strong_password(password):
                return 'Password does not meet the requirements. Please try again.'

            # Register the user
            hashed_password, salt = hash_password(password)
            users[username] = {'hashed_password': hashed_password, 'salt': salt}
            return 'Registration successful! You can now login.'

        elif 'login' in request.form:
            # Log the login attempt
            logging.info(f'Login attempt for username: {username}')
            # Attempt login
            if username in users and verify_password(password, users[username]['hashed_password'], users[username]['salt']):
                session['username'] = username  # Store username in session
                return redirect(url_for('welcome'))

            else:
                return 'Login failed. Incorrect username or password.'

    return render_template('index.html')

@app.route('/welcome')
def welcome():
    username = session.get('username')
    if username:
        return f'Welcome, {username}! You are logged in.'
    else:
        return 'You need to log in.'

@app.route('/view_logs')
def view_logs():
    try:
        with open('login_attempts.log', 'r') as log_file:
            log_content = log_file.read()
    except FileNotFoundError:
        log_content = 'Log file not found.'

    return render_template('logs.html', log_content=log_content)

if __name__ == '__main__':
    app.run(debug=True)
