import json
import bcrypt

def register():
    username = input("Enter your desired username: ")
    password = input("Enter your desired password: ")
    security_question = input("Enter a security question: ")
    security_answer = input("Enter the answer to your security question: ")

    # Hash the password with a random salt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # Store the username, hashed password, security question, and security answer in a dictionary
    user_data = {
        'username': username,
        'hashed_password': hashed_password.decode(),  # Convert bytes to string for JSON serialization
        'security_question': security_question,
        'security_answer': security_answer
    }

    # Write the user data to a file or database
    with open('user_data.json', 'a') as file:
        file.write(json.dumps(user_data) + '\n')

    print("Registration successful!")

def reset_password():
    username = input("Enter your username: ")
    security_question = input("Enter your security question: ")
    security_answer = input("Enter the answer to your security question: ")

    # Read the user data from the file or database
    with open('user_data.json', 'r') as file:
        for line in file:
            user_data = json.loads(line)
            if user_data['username'] == username:
                stored_security_question = user_data['security_question']
                stored_security_answer = user_data['security_answer']
                if security_question == stored_security_question and security_answer == stored_security_answer:
                    new_password = input("Enter your new password: ")

                    # Hash the new password with a random salt
                    hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())

                    # Update the hashed password in the user data
                    user_data['hashed_password'] = hashed_password.decode()

                    # Rewrite the updated user data to the file or database
                    with open('user_data.json', 'w') as file:
                        file.write(json.dumps(user_data) + '\n')

                    print("Password reset successful!")
                    return

    print("Invalid username or security question/answer. Please try again.")

register()
reset_password()
