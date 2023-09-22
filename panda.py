import pandas as pd

# Sample restaurant sales data
data = {
    'Food Item': ['Burger', 'Pizza', 'Pasta', 'Salad', 'Soda'],
    'Quantity Sold': [150, 200, 100, 50, 300],
    'Price per Item': [5.99, 8.99, 7.49, 4.99, 1.99]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Create a Pandas Excel writer using XlsxWriter as the engine
writer = pd.ExcelWriter('restaurant_sales.xlsx', engine='xlsxwriter')

# Write the DataFrame to the Excel file
df.to_excel(writer, sheet_name='Sales Data', index=False)

# Get the xlsxwriter workbook and worksheet objects
workbook = writer.book
worksheet = writer.sheets['Sales Data']

# Add a format for currency
money_format = workbook.add_format({'num_format': '$#,##0.00'})

# Apply the format to the appropriate columns
worksheet.set_column('C:C', None, money_format)

# Save the Excel file
writer.save()
