import csv

def convert_csv_to_array(input_csv_path, output_python_path):
    data = []
    with open(input_csv_path, "r") as input_file:
        csv_reader = csv.reader(input_file)
        for row in csv_reader:
            if row:
                data.append(row[0])

    with open(output_python_path, "w") as data_file:
        data_file.write(f'data = {data}')

if __name__ == "__main__":
  convert_csv_to_array("output.csv", "summarised_book_chunks.py")