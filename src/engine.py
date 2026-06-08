from src.utils import top_k_heap

class RecommendationEngine:

    def __init__(self, products, users, popularity):
        self.products = products
        self.users = users
        self.popularity = popularity

    def jaccard(self, a, b):
        if not a or not b:
            return 0
        return len(a & b) / len(a | b)

    def score_product(self, user, product):
        score = 0
        reasons = []

        # 1. Preference
        if product.category in user.preferences:
            score += 40
            reasons.append("Matches preference")

        # 2. Rating
        rating_score = product.rating * 15
        score += rating_score

        # 3. Popularity
        pop = self.popularity.get(product.id, 0)
        score += pop * 0.8
        if pop > 40:
            reasons.append("Highly popular")

        # 4. PURCHASE BOOST
        if product.id in user.purchases:
            score += 100
            reasons.append("Based on your purchase")

        # 5. Collaborative Filtering
        cf_score = 0
        for other in self.users.values():
            if other.id == user.id:
                continue

            sim = self.jaccard(user.purchases, other.purchases)

            if product.id in other.purchases:
                cf_score += sim * 100

        score += cf_score

        if cf_score > 0:
            reasons.append("Similar users liked")

        return score, reasons

    def recommend(self, user_id, k=5):
        user = self.users[user_id]
        scored = []

        for p in self.products:
            score, reasons = self.score_product(user, p)
            scored.append((score, p, reasons))

        return top_k_heap(scored, k)

    def search(self, query):
        query = query.lower()
        return [p for p in self.products if query in p.name.lower()]