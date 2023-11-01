import csv

# Input CSV file path
input_csv_path = "input.csv"

# Initialize an empty list to store the values from the first column
data = []

# Read the input CSV file
with open(input_csv_path, "r") as input_file:
    csv_reader = csv.reader(input_file)

    # Process each row in the CSV file
    for row in csv_reader:
        if row:
            # Append the value from the first column to the data list
            data.append(row[0])

# Write the data list to a Python file as a variable
with open("data.py", "w") as data_file:
    data_file.write(f'data = {data}')

print("CSV to array conversion complete.")