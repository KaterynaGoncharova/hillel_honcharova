"""1"""
import csv

file_path_1 = '/Users/katerynagoncharova/random.csv'
file_path_2 = '/Users/katerynagoncharova/random-michaels.csv'

data = []

def read_csv_file(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(tuple(row))

read_csv_file(file_path_1)
read_csv_file(file_path_2)

unique_data = list(set(data))

result_file_path = 'result_goncharova.csv'
with open(result_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(unique_data)

print(f" Result in {result_file_path}")

"""2"""
import json
import logging

logging.basicConfig(filename='json__goncharova.log', level=logging.ERROR)

file_paths = [
    '/Users/katerynagoncharova/localization.en.json',
    '/Users/katerynagoncharova/localization.ru.json',
    '/Users/katerynagoncharova/swagger.json',
    '/Users/katerynagoncharova/login.json'
]

for file_path in file_paths:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file) 
        print(f"{file_path} - Valid JSON")
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logging.error(f"Invalid JSON in {file_path}: {e}")
        print(f"{file_path} - Invalid JSON. Error logged.")

"""3"""
import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_incoming_by_group_number(file_path, group_number):
    try:
        root = ET.parse(file_path).getroot()

        group = next((g for g in root.findall('group') if g.findtext('number') == group_number), None)

        if group:
            incoming = group.findtext('timingExbytes/incoming')
            message = f"Group number: {group_number}, incoming: {incoming}" if incoming else f"Group number: {group_number} has no incoming element."
        else:
            message = f"Group number: {group_number} not found."

        logging.info(message)
    except ET.ParseError as e:
        logging.error(f"Failed to parse XML file: {e}")

file_path = '/Users/katerynagoncharova/groups.xml'
group_number = '2'
find_incoming_by_group_number(file_path, group_number)