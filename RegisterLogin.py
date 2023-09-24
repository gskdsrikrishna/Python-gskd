import bcrypt
import json

def register():
    username = input("Enter your desired username: ")
    password = input("Enter your desired password: ")

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # Store the username and hashed password in a dictionary
    user_data = {
        'username': username,
        'hashed_password': hashed_password.decode()  # Convert bytes to string for JSON serialization
    }

    # Write the user data to a file or database
    with open('user_data.json', 'a') as file:
        file.write(json.dumps(user_data) + '\n')

    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Read the user data from the file or database
    with open('user_data.json', 'r') as file:
        for line in file:
            user_data = json.loads(line)
            if user_data['username'] == username:
                stored_password = user_data['hashed_password'].encode()
                if bcrypt.checkpw(password.encode(), stored_password):
                    print("Login successful!")
                    return

    print("Invalid username or password. Please try again.")

register()
login()
