import streamlit as st

st.set_page_config(
    page_title="Auto Workshop Dashboard",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Auto Workshop Dashboard")

st.markdown("---")
st.subheader("🔧 Services")

col1, col2, col3 = st.columns(3)

col1.metric("Total Services", 5)
col2.metric("Completed", 3)
col3.metric("Pending", 2)

st.markdown("### 📋 Services List")
st.markdown("---")

import pandas as pd

st.title("🚗 Auto Workshop Services")

data = pd.DataFrame({
    "Service": [
        "Car Painting",
        "Android Installation",
        "Rim Installation",
        "Seat Cover Change",
        "Car Upgrading"
    ],
    "Price (Tsh)": [500000, 250000, 150000, 120000, 800000],
    "Status": ["Completed", "Completed", "Pending", "Completed", "Pending"]
})

st.subheader("🔧 Services List")
st.dataframe(data)

st.subheader("📊 Price Overview")
st.bar_chart(data.set_index("Service")["Price (Tsh)"])

st.metric("Total Services", len(data))
st.metric("Completed", len(data[data["Status"] == "Completed"]))
st.metric("Pending", len(data[data["Status"] == "Pending"]))
st.subheader("📲 Book a Service via WhatsApp")

phone_number = "255718632621"

service = st.selectbox(
    "Choose a service",
    ["Car Painting", "Android Installation", "Rim Installation", "Seat Cover Change", "Car Upgrading"]
)

message = f"Hello, I want to book: {service} at your workshop."

whatsapp_url = f"https://wa.me/{phone_number}?text={message}"

st.markdown(f"[📲 Click here to book on WhatsApp]({whatsapp_url})")
