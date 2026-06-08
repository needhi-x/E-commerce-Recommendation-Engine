def recommend_products(user, products, popularity):
    results = []

    for product in products:
        # -------- SCORING SYSTEM --------
        pref_score = 40 if product.category == user.preference else 0
        rating_score = product.rating * 15
        pop_score = popularity.get(product.name.lower(), 0)

        total_score = pref_score + rating_score + pop_score

        results.append({
            "name": product.name,
            "category": product.category,
            "rating": product.rating,
            "score": total_score,
            "match_pref": product.category == user.preference,
            "popular": pop_score > 40
        })

    # -------- SORT BY SCORE --------
    results.sort(key=lambda x: x["score"], reverse=True)

    return results