import pandas as pd

# Create a sample DataFrame
data = {'col1': [1, 2, 3, 4, 5], 'col2': ['A', 'B', 'C', 'D', 'E']}
df = pd.DataFrame(data)

# Save to an Excel file
df.to_excel("MigracionExcelCsv/sample.xlsx", index=False)
