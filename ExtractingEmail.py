import re

# Extracting email addresses from text
text = "Contact us at info@example.com or support@example.com"
email_addresses = re.findall(r'[\w\.-]+@[\w\.-]+', text)
print(email_addresses)  # Output: ['info@example.com', 'support@example.com']

# Extracting dates in 'YYYY-MM-DD' format
text = "Date: 2023-06-24"
date = re.search(r'\d{4}-\d{2}-\d{2}', text)
if date:
    print(date.group())  # Output: '2023-06-24'