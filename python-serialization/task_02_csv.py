#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert data from a CSV file to JSON format and save it to data.json.

    Args:
        csv_filename (str): Name of the CSV file.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except (FileNotFoundError, OSError):
        return False
