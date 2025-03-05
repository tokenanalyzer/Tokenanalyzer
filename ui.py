import streamlit as st
import requests

# Set page layout like Play Store
st.set_page_config(page_title="TokenAnalyzer", page_icon="📊", layout="wide")

# App Header
st.title("🚀 TokenAnalyzer - AI Crypto Insights")
st.markdown("**Track, analyze & predict crypto trends with AI-powered insights.**")

# Sidebar - Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Trending Tokens", "AI Predictions", "Portfolio"])

# Backend API URL (Change this if needed)
API_URL = "http://127.0.0.1:5000/api/token"

# Home Page
if page == "Home":
    st.subheader("📊 Live Market Data")
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            tokens = response.json()
            for token in tokens:
                st.metric(label=f"{token['name']} ({token['symbol']})", 
                          value=f"${token['price']}", 
                          delta=f"{token['change_24h']}%")
        else:
            st.error("Failed to fetch data.")
    except Exception as e:
        st.error(f"Error: {e}")

# Trending Tokens
elif page == "Trending Tokens":
    st.subheader("🔥 Top Gainers & Trending Coins")
    st.info("Coming soon...")

# AI Predictions
elif page == "AI Predictions":
    st.subheader("🤖 AI-Based Crypto Predictions")
    st.info("Coming soon...")

# Portfolio
elif page == "Portfolio":
    st.subheader("💼 Your Portfolio")
    st.warning("Login required to view portfolio.")
