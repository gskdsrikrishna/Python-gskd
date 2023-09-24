def app_lock_screen(password):
    entered_password = input("Enter the password to unlock the app: ")
    if entered_password == password:
        print("Access granted. App unlocked.")
        # Add your code here to launch the protected application
    else:
        print("Incorrect password. Access denied.")

# Example usage
protected_app_password = "1234"  # Replace with your desired password
app_lock_screen(protected_app_password)\