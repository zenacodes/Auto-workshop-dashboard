import streamlit as st
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
