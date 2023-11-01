import csv
import json

# Get specialist data
specialists = []

with open('examples/data/example_requests_to_chat_completion_results.jsonl', 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line)
        specialists.append(data)

# Create a CSV file for writing
with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(['Original Data', 'Generated Bio'])

    # Iterate through the specialists and write data to the CSV
    for specialist in specialists:
        original_data = specialist[0]['messages'][1]['content']
        generated_bio = specialist[1]['choices'][0]['message']['content']

        # Write data to the CSV file
        csv_writer.writerow([original_data, generated_bio])

print("CSV file created successfully.")