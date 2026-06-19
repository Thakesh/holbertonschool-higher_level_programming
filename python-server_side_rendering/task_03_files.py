#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def load_json_data():
    """Load data from JSON file."""
    with open("products.json", "r", encoding="utf-8") as file:
        return json.load(file)


def load_csv_data():
    """Load data from CSV file."""
    products = []

    with open("products.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)

    return products


@app.route("/products")
def products():
    """Display products from JSON or CSV."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        data = load_json_data()
    elif source == "csv":
        data = load_csv_data()
    else:
        return render_template(
            "product_display.html",
            error="Wrong source"
        )

    if product_id:
        filtered = [
            product for product in data
            if str(product.get("id")) == product_id
        ]

        if not filtered:
            return render_template(
                "product_display.html",
                error="Product not found"
            )

        data = filtered

    return render_template(
        "product_display.html",
        products=data
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
