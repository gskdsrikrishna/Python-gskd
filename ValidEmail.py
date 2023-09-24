#95.Check if a string is a valid email address
import re

email = input("Enter an email address: ")

is_valid_email = re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None
if is_valid_email:
    print(email, "is a valid email address.")
else:
    print(email, "is not a valid email address.")