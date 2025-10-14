import streamlit as st
import pandas as pd
import plotly.express as px

from bidding_logic import auto_bid

st.set_page_config(page_title="Automated Bidding Assistant", page_icon="🤖", layout="wide")

st.title("🤖 Automated Bidding Assistant")

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


data = load_data("data/auctions.csv")

st.subheader("📦 Active Auctions")
st.dataframe(data, use_container_width=True)

with st.sidebar:
    st.header("Controls")
    max_budget = st.slider("Total max budget ($)", 100, 5000, 1000, step=50)
    max_bid_per_item = st.slider("Max bid per item ($)", 50, 2000, 800, step=25)
    snipe_minutes = st.slider("Snipe window (minutes)", 1, 30, 5)
    run = st.button("Run Auto-Bid")

if run:
    results = auto_bid(data, max_budget=max_budget, max_bid_per_item=max_bid_per_item, snipe_minutes=snipe_minutes)
    results_df = pd.DataFrame(results)

    st.success("✅ Auto-bidding complete!")
    st.subheader("📄 Bid Results")
    st.dataframe(results_df, use_container_width=True)

    st.subheader("📈 Bid Summary")
    if not results_df.empty:
        by_item = results_df.groupby("item_name", as_index=False)["bid_amount"].sum()
        fig = px.bar(by_item, x="item_name", y="bid_amount", title="Total Bid Amount by Item")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No bids placed based on the current settings.")
else:
    st.info("Set your preferences in the sidebar and click 'Run Auto-Bid'.")
