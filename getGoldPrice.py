import streamlit as st
import requests

st.set_page_config(page_title="محاسبه قیمت طلای ۱۸ عیار", page_icon="🟡")

def get_gold_price_usd():
    url = "https://api.metals.live/v1/spot"
    data = requests.get(url).json()
    return next(item[1] for item in data if item[0] == "gold")

st.title("🟡 محاسبه قیمت طلای ۱۸ عیار")

usd_to_rial = st.number_input("💵 نرخ دلار (ریال)", min_value=100000, step=1000)

if st.button("محاسبه"):
    gold_ounce = get_gold_price_usd()
    gram_18 = (gold_ounce * usd_to_rial / 31.1035) * 0.75
    st.success(f"اونس جهانی: {gold_ounce:.2f} دلار")
    st.write(f"💰 قیمت هر گرم طلای ۱۸ عیار: **{gram_18:,.0f} ریال**")
