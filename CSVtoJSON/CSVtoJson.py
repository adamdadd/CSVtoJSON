#!/usr/bin/python

import sys, getopt
import csv
import json
import math

#Get Command Line Arguments
def main(argv):
    print("CSV to JSON Converter")
    print("Adding .csv and .json not required....................")
    input_file = input("Name of CSV file: ") + ".csv"
    output_file = input("Desired name of JSON file: ") + ".json"
    format = "pretty"

    read_csv(input_file, output_file, format)
    print("Conversion Complete!")

#Read CSV File
def read_csv(file, json_file, format):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        print("Reading CSV file...............")
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        for field in csv_rows:
            for el in field:
                if type(field[el]) != float:
                    try:
                        field[el] = float(field[el])
                    except:
                        continue
                else:
                    continue
        write_json(csv_rows, json_file, format)

#Convert csv data into json and write it
def write_json(data, json_file, format):
    print("Writing JSON file.............")
    with open(json_file, "w") as f:
        if format == "pretty":
            f.write(json.dumps(data, sort_keys = False, indent=2, separators=(',', ': '),ensure_ascii=False))
        else:
            f.write(json.dumps(data))

if __name__ == "__main__":
   main(sys.argv[1:])

