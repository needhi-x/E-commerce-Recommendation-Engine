from collections import defaultdict


class RecommendationEngine:

    def __init__(self, products, users, popularity):
        self.products = products
        self.users = users
        self.popularity = popularity

        # 📂 Category index
        self.category_index = defaultdict(list)
        for p in self.products:
            self.category_index[p.category].append(p)

    # 🔥 MAIN RECOMMEND FUNCTION
    def recommend(self, user_id, top_n=5):
        user = self.users.get(user_id)

        # ❌ No user → show trending
        if not user:
            return [(p, ["🔥 Trending product"]) for p in self.trending_products(top_n)]

        scored = []

        for product in self.products:
            score, reasons = self._compute_score_with_reason(user, product)
            scored.append((score, product, reasons))

        # Sort by score
        scored.sort(key=lambda x: x[0], reverse=True)

        return [(p, r) for _, p, r in scored[:top_n]]

    # 🧠 CORE SCORING LOGIC
    def _compute_score_with_reason(self, user, product):
        score = 0
        reasons = []

        # 🎯 Preference match
        if product.category in user["preferences"]:
            score += 120
            reasons.append("🎯 For you")

        # ⭐ Rating (used in score)
        score += product.rating * 25

        if product.rating >= 4.5:
            reasons.append("⭐ Top rated")

        # 🔥 Popularity
        pop = self.popularity.get(product.id, 0)
        score += pop * 2

        if pop > 40:
            reasons.append("🔥 Popular")
        elif pop > 20:
            reasons.append("📈 Trending")

        return score, reasons

    # 🔥 TRENDING PRODUCTS
    def trending_products(self, top_n=5):
        return sorted(
            self.products,
            key=lambda p: (self.popularity.get(p.id, 0), p.rating),
            reverse=True
        )[:top_n]

    # 📂 CATEGORY BASED RECOMMENDATION
    def recommend_by_category(self, category, top_n=5):
        category = category.lower()
        products = self.category_index.get(category, [])

        return sorted(
            products,
            key=lambda p: (p.rating, self.popularity.get(p.id, 0)),
            reverse=True
        )[:top_n]

    # 🔍 SMART SEARCH (PREFIX + CONTAINS)
    def search_products(self, query, limit=5):
        query = query.lower().strip()

        prefix = []
        contains = []

        for p in self.products:
            name = p.name.lower()

            if name.startswith(query):
                prefix.append(p)
            elif query in name:
                contains.append(p)

        results = prefix + contains

        return sorted(
            results,
            key=lambda p: (p.rating, self.popularity.get(p.id, 0)),
            reverse=True
        )[:limit]