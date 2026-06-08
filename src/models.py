class Product:
    def __init__(self, id, name, category, rating):
        self.id = id
        self.name = name
        self.category = category
        self.rating = rating


class User:
    def __init__(self, id, preferences=None, purchases=None):
        self.id = id
        self.preferences = preferences if preferences else set()
        self.purchases = purchases if purchases else set()