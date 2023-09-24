import pandas as pd

# Create a DataFrame
data = {'Column1': [1, 2, 3, 4, 5],
        'Column2': ['A', 'B', 'C', 'D', 'E']}
df = pd.DataFrame(data)

# Write DataFrame to Excel file
df.to_excel('new_file.xlsx', index=False)
