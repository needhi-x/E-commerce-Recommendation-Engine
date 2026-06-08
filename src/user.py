class User:
    def __init__(self, id, preferences, purchases):
        self.id = id
        self.preferences = preferences
        self.purchases = purchases
        self.search_history = []   # ✅ REQUIRED