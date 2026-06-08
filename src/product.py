class Product:
    def __init__(self, pid, name, category, rating, price):
        self.pid = pid
        self.name = name
        self.category = category.lower()
        self.rating = rating
        self.price = price

    def __repr__(self):
        return f"{self.name} (ID:{self.pid}, {self.category}, ⭐{self.rating}, ₹{self.price})"