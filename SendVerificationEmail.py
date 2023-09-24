import bcrypt
import json
import random
import smtplib

def send_verification_email(email, verification_code):
    # Replace the placeholders with your email server details
    smtp_server = 'your_smtp_server'
    smtp_port = 587
    smtp_username = 'your_smtp_username'
    smtp_password = 'your_smtp_password'

    sender_email = 'your_sender_email'
    subject = 'Verification Code for MFA'

    message = f"Your verification code is: {verification_code}"

    # Connect to the email server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(sender_email, email, f"Subject: {subject}\n\n{message}")
    server.quit()

def register():
    username = input("Enter your desired username: ")
    password = input("Enter your desired password: ")
    email = input("Enter your email address: ")

    # Hash the password with a random salt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # Generate a random verification code
    verification_code = str(random.randint(100000, 999999))

    # Store the username, hashed password, email, and verification code in a dictionary
    user_data = {
        'username': username,
        'hashed_password': hashed_password.decode(),  # Convert bytes to string for JSON serialization
        'email': email,
        'verification_code': verification_code,
        'is_verified': False
    }

    # Write the user data to a file or database
    with open('user_data.json', 'a') as file:
        file.write(json.dumps(user_data) + '\n')

    # Send the verification code to the user's email
    send_verification_email(email, verification_code)

    print("Registration successful! Please check your email for the verification code.")

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
                    if user_data['is_verified']:
                        print("Login successful!")
                        return
                    else:
                        verification_code = input("Enter the verification code sent to your email: ")
                        if verification_code == user_data['verification_code']:
                            user_data['is_verified'] = True

                            # Update the user data in the file or database
                            with open('user_data.json', 'w') as file:
                                file.write(json.dumps(user_data) + '\n')

                            print("Login successful!")
                            return
                        else:
                            print("Invalid verification code. Please try again.")

    print("Invalid username or password. Please try again.")

register()
login()
