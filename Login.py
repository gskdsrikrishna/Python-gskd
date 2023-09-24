def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Predefined set of credentials
    predefined_username = "admin"
    predefined_password = "password123"

    if username == predefined_username and password == predefined_password:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")

login()
