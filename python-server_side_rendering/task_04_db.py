#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def load_json_data():
    """Load products from JSON."""
    with open("products.json", "r", encoding="utf-8") as file:
        return json.load(file)


def load_csv_data():
    """Load products from CSV."""
    products = []

    with open("products.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            products.append(row)

    return products


def load_sql_data():
    """Load products from SQLite database."""
    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")

    products = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return products


@app.route("/products")
def products():
    """Display products from the selected source."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    try:
        if source == "json":
            data = load_json_data()

        elif source == "csv":
            data = load_csv_data()

        elif source == "sql":
            data = load_sql_data()

        else:
            return render_template(
                "product_display.html",
                error="Wrong source"
            )

    except Exception:
        return render_template(
            "product_display.html",
            error="Database error"
        )

    if product_id:
        data = [
            product for product in data
            if str(product.get("id")) == product_id
        ]

        if not data:
            return render_template(
                "product_display.html",
                error="Product not found"
            )

    return render_template(
        "product_display.html",
        products=data
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
