import pandas as pd

# Read CSV file into DataFrame
df = pd.read_excel('automated_dtr/templates/skibidi.xlsx')
count = 0
# Lawrence time
skibidi = df.iloc[4, 0]
# Name
skibidi = df.iloc[3, 10]

if pd.isna(skibidi):
    print("skib")
else:
    print(skibidi)
    
# print(df.iloc[2, 0])
# ID AND NAMES
# for x in range(3, len(df)):
#     id = df.iloc[x, 0]
#     name = df.iloc[x, 1]
#     dept = df.iloc[x, 2]
#     company = df.iloc[x, 3]

# for x in range(3, len(df)): 
#     id = df.iloc[x, 0]
#     name = df.iloc[x, 1]
#     time_in = df.iloc[x + 1, 9]
#     time_out = df.iloc[x + 1, 10]
#     print(f"ID: {id} Name: {name}")
#     print(f"Time In: {time_in} Time Out: {time_out}")
#     count += 1

    # print(f"ID: {id} Name: {name} Dept: {dept} Company {company}")
    # print(f"Processing row {x}")
    # count+=1

















# val = df.iloc[2, 1]
# print(val)

# columns_list = list(df.columns)
# print(columns_list)

# file = r'automated_dtr/templates/12_StandardReport.xls'
# # Read the Excel file into a DataFrame using the xlrd engine
# df = pd.read_excel(file, engine='openpyxl')

# # Print the DataFrame
# print(df.head())