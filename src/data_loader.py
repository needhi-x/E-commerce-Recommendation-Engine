import csv
from models import Product

product_popularity = {
    1: 50, 2: 45, 3: 30,
    4: 60, 5: 40, 6: 20,
    7: 35, 8: 25, 9: 15,
    10: 55
}

def load_products(file_path="data/products.csv"):
    products = []
    with open(file_path, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(Product(
                row["id"],
                row["name"],
                row["category"],
                row["price"],
                row["rating"],
                row.get("image_url", "https://picsum.photos/200")
            ))
    return products


def load_users(file_path="data/users.csv"):
    users = {}
    with open(file_path, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users[int(row["id"])] = {
                "preferences": [row["preferences"].strip().lower()]
            }
    return users