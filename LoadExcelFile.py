import pandas as pd

# Load the Excel file
data = pd.read_excel('filename.xlsx', sheet_name='Sheet1')

# Access specific worksheet
worksheet = data['Sheet1']

# Access specific rows
rows = worksheet.loc[0:5]  # Example: Get rows 0 to 5

# Access specific columns
columns = worksheet[['Column1', 'Column2']]  # Example: Get columns 'Column1' and 'Column2'
