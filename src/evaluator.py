def baseline(products, k=5):
    return sorted(products, key=lambda p: p.rating, reverse=True)[:k]

def compare(engine, user_id):
    before = baseline(engine.products)
    after = engine.recommend(user_id)
    return before, after