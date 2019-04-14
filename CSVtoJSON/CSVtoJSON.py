#!/usr/bin/env python3
"""CSVtoJSON"""

import sys
import csv
import json

def main(argv):
    """Get Commandline Arguements"""
    print("CSV to JSON Converter")
    print("Adding .csv and .json not required....................")
    input_file = input("Name of CSV file: ") + ".csv"
    output_file = input("Desired name of JSON file: ") + ".json"
    format_type = "pretty"

    read_csv(input_file, output_file, format_type)
    print("Conversion Complete!")

def read_csv(file, json_file, format_type):
    """Reads CSV file"""
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        print("Reading CSV file!")
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        for field in csv_rows:
            for element in field:
                if not isinstance(field[element], float):
                    try:
                        field[element] = float(field[element])
                    except Exception as error:
                        print(error)
                        continue
                else:
                    continue
        write_json(csv_rows, json_file, format_type)

def write_json(data, json_file, format_type):
    """Converts data and writes JSON output file"""
    print("Writing JSON file!")
    with open(json_file, "w") as file_json:
        if format_type == "pretty":
            file_json.write(json.dumps(data, sort_keys=False, indent=2,
                                       separators=(',', ': '), ensure_ascii=False))
        else:
            file_json.write(json.dumps(data))

if __name__ == "__main__":
    main(sys.argv[1:])
