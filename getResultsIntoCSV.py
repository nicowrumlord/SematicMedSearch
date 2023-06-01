import csv
import os

def saveResults(prompt, data):
    file_name = "document_scores.csv"
    header_row = ['prompt']
    header_row.extend([f"doc{i+1}" for i in range(len(data))])

    if os.path.exists(file_name):
    
        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            values = [result[1] for result in data]
            prompt_values = [prompt]
            prompt_values.extend(values)

            # Write prompt values to the CSV file
            writer.writerow(prompt_values) 
              

    else:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header_row)
            values = [result[1] for result in data]
            prompt_values = [prompt]
            prompt_values.extend(values)

            # Write prompt values to the CSV file
            writer.writerow(prompt_values) 