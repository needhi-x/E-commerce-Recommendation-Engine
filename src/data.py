from src.models import Product, User


def load_products():
    return [
        Product(1, "iphone", "electronics", 4.8),
        Product(2, "macbook", "electronics", 4.7),
        Product(3, "headphones", "electronics", 4.6),
        Product(4, "watch", "electronics", 4.6),
        Product(5, "laptop", "electronics", 4.5),
        Product(6, "speaker", "electronics", 4.3),
        Product(7, "tshirt", "fashion", 4.2),
        Product(8, "jeans", "fashion", 4.3),
        Product(9, "sofa", "home", 4.4),
        Product(10, "lamp", "home", 4.1),
    ]


from src.models import User

def load_users():
    return [
        User(1, {"electronics"}, {101, 102}),
        User(2, {"fashion"}, {103}),
        User(3, {"home"}, set())
    ]


def load_popularity():
    return {
        "iphone": 50,
        "macbook": 45,
        "headphones": 55,
        "watch": 35,
        "laptop": 30,
        "speaker": 38,
        "tshirt": 60,
        "jeans": 42,
        "sofa": 25,
        "lamp": 20,
    }