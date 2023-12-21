#!/usr/bin/env python3
import os
import csv
from argparse import ArgumentParser
from fontquant import quantify

__doc__ = """
This script should:

1. Iterate over all the fonts in a given directory (CMD arg)
2. Find the 'Regular' weight file
3. Process it through font quant
4. Save the results in a dictionary
5. Process/output the results in .CSV format

"""

def findRegularFilePaths(main_directory, file_extension, weight_filter="regular"):
    """docstring for findRegularFiles"""
    paths = []
    for root, dirs, files in os.walk(main_directory):
        for file in files:
            if file.lower().endswith(weight_filter + '.' + file_extension):
                paths.append(os.path.join(root, file))
            elif file.endswith('].' + file_extension) and 'Italic' not in file:
                paths.append(os.path.join(root, file))
    return paths

def checkWeight(file_path):
    """docstring for fname"""
    data = []
    results = quantify(file_path)
    value = results["appearance"]["weight"]["value"]
    if value:
        data = (file_path.split("/")[-2], value)
        print(file_path.split("/")[-2])
    return data

def save_to_csv(raw_data, csv_filename, secondary_field_name):
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ['Font name', secondary_field_name]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for d in raw_data:
            writer.writerow({'Font name': d[0], secondary_field_name: d[1]})

parser = ArgumentParser()
parser.add_argument('directory')
parser.add_argument('output')

def main(args=None):
    """Run all edits"""
    args = parser.parse_args(args)
    source_path = args.directory
    file_path = args.output
    weight_data = []
    if source_path:
        all_paths = findRegularFilePaths(source_path, "ttf")
        if len(all_paths) > 0:
            for path in all_paths:
                weight_data.append(checkWeight(path))
    if weight_data:
        save_to_csv(weight_data, file_path, 'Weight')
    else:
        print("no path found")

if __name__ == '__main__':
    main()
