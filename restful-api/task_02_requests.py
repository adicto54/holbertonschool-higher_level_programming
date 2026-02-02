#!/usr/bin/python3
"""
Task 02: Consuming and processing data from an API using Python
"""

import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints their titles
    """
    response = requests.get(URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them to posts.csv
    """
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            writer.writerows(structured_posts)
