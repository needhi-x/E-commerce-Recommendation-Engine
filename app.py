import streamlit as st
import matplotlib.pyplot as plt
from src.data import load_products, load_users, load_popularity
from src.engine import RecommendationEngine

st.set_page_config(layout="wide")

# ---------------- INIT ----------------
if "products" not in st.session_state:
    st.session_state.products = load_products()
    st.session_state.users = load_users()
    st.session_state.popularity = load_popularity()

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Controls")

user_index = st.sidebar.selectbox(
    "Select User",
    list(range(len(st.session_state.users))),
    format_func=lambda i: f"User {st.session_state.users[i].id}"
)

user = st.session_state.users[user_index]

# Preference change (FIXED)
new_pref = st.sidebar.selectbox(
    "Change Preference",
    ["electronics", "fashion", "home"]
)

if st.sidebar.button("Apply Preference"):
    user.preferences = {new_pref}
    st.sidebar.success("Preference Updated!")

# ---------------- ENGINE ----------------
engine = RecommendationEngine(
    st.session_state.products,
    {u.id: u for u in st.session_state.users},
    st.session_state.popularity
)

# ---------------- UI HEADER ----------------
st.markdown(
    """
    <h1 style='text-align:center; color:#4ADE80;'>
    🛒 Smart Recommendation Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)

# ---------------- SEARCH ----------------
st.subheader("🔍 Search Product")

query = st.text_input("Type product name...")

results = []

if query:
    results = engine.search(query)

# ---------------- RECOMMEND ----------------
recommendations = engine.recommend(user.id, 5)

# ---------------- DISPLAY ----------------
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🛍️ Products")

    display_list = results if query else [r[1] for r in recommendations]

    for p in display_list:
        score, reasons = engine.score_product(user, p)

        st.markdown(f"""
        <div style="
            background:#1f2937;
            padding:15px;
            border-radius:10px;
            margin-bottom:10px;
        ">
        <h4 style="color:#60A5FA;">{p.name.title()}</h4>
        <p>📂 {p.category} | ⭐ {p.rating}</p>
        <p style="color:#FBBF24;">Score: {round(score,2)}</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.subheader("📈 Recommendation Graph")

    names = [r[1].name for r in recommendations]
    scores = [r[0] for r in recommendations]

    fig, ax = plt.subplots()

    ax.plot(names, scores, marker='o')

    ax.set_facecolor("#1f2937")
    fig.patch.set_facecolor("#141E30")

    ax.set_xlabel("Products", color="white")
    ax.set_ylabel("Score", color="white")

    ax.tick_params(colors='white')

    st.pyplot(fig)

# ---------------- COMPARISON ----------------
st.subheader("⚖️ Model Comparison")

col3, col4 = st.columns(2)

with col3:
    st.markdown("### ❌ Baseline")
    baseline = sorted(
        st.session_state.products,
        key=lambda x: x.rating,
        reverse=True
    )[:5]

    for p in baseline:
        st.write(f"{p.name} ({p.rating})")

with col4:
    st.markdown("### ✅ Improved")

    for score, p, _ in recommendations:
        st.write(f"{p.name} ({round(score,1)})")

# ---------------- USER DATA ----------------
st.subheader("📊 User Insights")

st.write("Preferences:", user.preferences)
st.write("Purchases:", list(user.purchases))