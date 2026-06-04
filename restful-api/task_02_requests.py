#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder and print their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()

        for post in data:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder and save them to a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        structured_data = []

        for post in data:
            structured_data.append({
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            })

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_data)


fetch_and_print_posts()

fetch_and_print_posts()
fetch_and_save_posts()
