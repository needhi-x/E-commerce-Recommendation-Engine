import sys
import os

# ✅ Fix import path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from data_loader import load_products, load_users, product_popularity
from recommendation_engine import RecommendationEngine

# ✅ Load data
products = load_products()
users = load_users()

# ✅ Initialize engine
engine = RecommendationEngine(products, users, product_popularity)


# 🔥 FUNCTION TO TEST USERS
def test_user(user_id):
    print("\n==============================")
    print(f"USER {user_id}")
    print("Preference:", users[user_id]["preferences"])
    print("==============================")

    recs = engine.recommend(user_id)   # ✅ recs defined here

    for i, (p, reasons) in enumerate(recs, 1):
        print(f"\n{i}. {p.name} | ₹{p.price}")

        if reasons:
            print("   ", " | ".join(reasons))


# ✅ RUN TESTS
test_user(1)
test_user(2)
test_user(3)


# 🔥 TRENDING
print("\n🔥 TRENDING")
trending = engine.trending_products()

for p in trending:
    print(f"{p.name} | ₹{p.price}")


# 📂 CATEGORY TEST
print("\n📂 ELECTRONICS")
electronics = engine.recommend_by_category("electronics")

for p in electronics:
    print(f"{p.name} | ₹{p.price}")


# 🔍 SEARCH TEST
print("\n🔍 SEARCH: 'ip'")
search_results = engine.search_products("ip")

for p in search_results:
    print(f"{p.name} | ₹{p.price}")