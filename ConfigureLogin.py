import bcrypt
import json
import logging
import datetime

# Configure logging
logging.basicConfig(filename='login_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Maximum number of allowed failed login attempts
MAX_LOGIN_ATTEMPTS = 3

# Lockout duration in minutes
LOCKOUT_DURATION = 5

# Dictionary to store failed login attempts
failed_login_attempts = {}

def log_login(username, status, ip_address):
    now = datetime.datetime.now()
    log_entry = f"Username: {username} - Status: {status} - IP Address: {ip_address}"
    logging.info(log_entry)

def register():
    username = input("Enter your desired username: ")
    password = input("Enter your desired password: ")

    # Hash the password with a random salt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # Store the username, hashed password, and access level in a dictionary
    user_data = {
        'username': username,
        'hashed_password': hashed_password.decode(),  # Convert bytes to string for JSON serialization
        'access_level': 'user'  # Default access level is 'user'
    }

    # Write the user data to a file or database
    with open('user_data.json', 'a') as file:
        file.write(json.dumps(user_data) + '\n')

    print("Registration successful!")

def login(ip_address):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the account is locked
    if username in failed_login_attempts and failed_login_attempts[username]['attempts'] >= MAX_LOGIN_ATTEMPTS:
        lockout_time = failed_login_attempts[username]['lockout_time']
        elapsed_time = datetime.datetime.now() - lockout_time
        if elapsed_time.total_seconds() < LOCKOUT_DURATION * 60:
            remaining_time = int((LOCKOUT_DURATION * 60 - elapsed_time.total_seconds()) / 60)
            print("Account is locked. Please try again after", remaining_time, "minutes.")
            return

    # Read the user data from the file or database
    with open('user_data.json', 'r') as file:
        for line in file:
            user_data = json.loads(line)
            if user_data['username'] == username:
                stored_password = user_data['hashed_password'].encode()
                if bcrypt.checkpw(password.encode(), stored_password):
                    access_level = user_data['access_level']

                    # Reset failed login attempts if login is successful
                    if username in failed_login_attempts:
                        del failed_login_attempts[username]

                    log_login(username, "Success", ip_address)
                    print("Login successful!")
                    print("Access Level:", access_level)
                    return
                else:
                    # Record failed login attempt
                    if username not in failed_login_attempts:
                        failed_login_attempts[username] = {'attempts': 1, 'lockout_time': datetime.datetime.now()}
                    else:
                        failed_login_attempts[username]['attempts'] += 1

                    # Lock the account if maximum login attempts exceeded
                    if failed_login_attempts[username]['attempts'] >= MAX_LOGIN_ATTEMPTS:
                        failed_login_attempts[username]['lockout_time'] = datetime.datetime.now()

                    log_login(username, "Failed", ip_address)
                    print("Invalid password. Please try again.")
                    return

    log_login(username, "Failed", ip_address)
    print("Invalid username. Please try again.")

register()
login("192.168.0.1")  # Example IP address, replace with actual IP address
