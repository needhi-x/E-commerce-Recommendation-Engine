import os

# ---------------- MODELS ----------------
class Product:
    def __init__(self, pid, name, category, price, rating):
        self.id = pid
        self.name = name
        self.category = category
        self.price = price
        self.rating = rating


class User:
    def __init__(self, preferences):
        self.preferences = set(preferences)
        self.cart = []
        self.purchase_history = []
        self.search_history = []


# ---------------- DATA ----------------
products = [
    Product(101, "Ultra HD Smart TV", "electronics", 59999, 4.7),
    Product(102, "iPhone Pro Max", "electronics", 125000, 4.8),
    Product(103, "Bluetooth Speaker", "electronics", 2999, 4.3),
    Product(104, "Running Shoes", "fashion", 1999, 4.2),
    Product(105, "Leather Jacket", "fashion", 4999, 4.5),
    Product(106, "Coffee Maker", "home", 3499, 4.1),
]

user = User(["electronics"])

popularity = {
    101: 90,
    102: 95,
    103: 80,
    104: 70,
    105: 85,
    106: 60
}


# ---------------- UI ----------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def header():
    print("\n" + "=" * 70)
    print("        🛒 E-COMMERCE CLI (ADVANCED)")
    print("=" * 70)


def pause():
    input("\nPress Enter to continue...")


# ---------------- SEARCH ----------------
def search_products(query):
    query = query.lower()
    return [
        p for p in products
        if query in p.name.lower() or query in p.category.lower()
    ]


# ---------------- SCORING ----------------
def score_product(user, product):
    score = product.rating

    if product.category in user.preferences:
        score += 2

    score += popularity[product.id] / 50

    return round(score, 2)


# ---------------- RECOMMEND ----------------
def recommend(user):
    scored = [(score_product(user, p), p) for p in products]
    scored.sort(reverse=True, key=lambda x: x[0])
    return scored[:5]


# ---------------- DISPLAY ----------------
def show_products(list_products):
    print("\n" + "=" * 60)
    print(f"{'ID':<5} {'PRODUCT':<25} {'CATEGORY':<12} {'PRICE'}")
    print("=" * 60)

    for p in list_products:
        print(f"{p.id:<5} {p.name:<25} {p.category:<12} ₹{p.price}")

    print("=" * 60)


def show_recommendations(user):
    recs = recommend(user)

    print("\n🔥 TOP RECOMMENDATIONS")
    print("=" * 70)
    print(f"{'Rank':<5} {'Score':<8} {'Product':<25} {'Reason'}")
    print("=" * 70)

    for i, (score, p) in enumerate(recs, 1):
        reasons = []

        if p.category in user.preferences:
            reasons.append("Preferred")

        if popularity[p.id] > 80:
            reasons.append("Popular")

        reason_text = ", ".join(reasons) if reasons else "General"

        print(f"{i:<5} {score:<8} {p.name:<25} {reason_text}")

    print("=" * 70)


def show_cart(user):
    print("\n🛒 YOUR CART")
    print("=" * 50)

    if not user.cart:
        print("Cart is empty")
    else:
        total = 0
        for p in user.cart:
            print(f"{p.id} - {p.name} ₹{p.price}")
            total += p.price

        print("\nTotal:", total)

    print("=" * 50)


def show_history(user):
    print("\n📜 HISTORY")
    print("=" * 50)

    print("\n🔍 Searches:")
    for s in user.search_history:
        print("•", s)

    print("\n🛒 Purchases:")
    for p in user.purchase_history:
        print("•", p)

    print("=" * 50)


# ---------------- MAIN ----------------
def main():
    clear()

    while True:
        header()

        print("\nMain Menu:")
        print("1. 🔍 Search Products")
        print("2. ⭐ Recommendations")
        print("3. 🛒 View Cart")
        print("4. 📜 History")
        print("5. ⚙️ Change Preference")
        print("6. ❌ Exit")

        choice = input("\nSelect option: ")

        # SEARCH
        if choice == "1":
            query = input("\nEnter search: ")
            results = search_products(query)

            user.search_history.append(query)

            if results:
                show_products(results)

                pid = input("\nEnter product ID to add to cart: ")
                for p in products:
                    if str(p.id) == pid:
                        user.cart.append(p)
                        print("✔ Added to cart")
            else:
                print("❌ No results found")

            pause()

        # RECOMMEND
        elif choice == "2":
            show_recommendations(user)

            pid = input("\nEnter product ID to add to cart: ")
            for p in products:
                if str(p.id) == pid:
                    user.cart.append(p)
                    print("✔ Added to cart")

            pause()

        # CART
        elif choice == "3":
            show_cart(user)

            print("\n1. Remove item")
            print("2. Checkout")
            print("3. Back")

            sub = input("Choose option: ")

            if sub == "1":
                pid = input("Enter product ID to remove: ")
                user.cart = [p for p in user.cart if str(p.id) != pid]
                print("✔ Removed")

            elif sub == "2":
                for p in user.cart:
                    user.purchase_history.append(p.name)

                user.cart.clear()
                print("✔ Purchase successful!")

            pause()

        # HISTORY
        elif choice == "4":
            show_history(user)
            pause()

        # PREF
        elif choice == "5":
            print("\nCategories: electronics, fashion, home")
            pref = input("Enter new preference: ").lower()
            user.preferences = {pref}
            print("✔ Updated")

            pause()

        # EXIT
        elif choice == "6":
            print("\n👋 Goodbye!")
            break

        else:
            print("Invalid choice")
            pause()


# ---------------- RUN ----------------
if __name__ == "__main__":
    main()