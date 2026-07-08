import csv
import json

def read_user_csv():
    with open("data/users.csv", newline = "" ) as file:
        reader = csv.DictReader(file)
        return list(reader)

def read_products_json():
    with open("data/products.json") as file:
        return json.load(file)

def read_checkout_csv():
    data = []
    with open("data/checkout_data.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data