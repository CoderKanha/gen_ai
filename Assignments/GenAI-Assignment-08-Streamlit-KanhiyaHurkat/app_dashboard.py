import streamlit as st

st.title("Sales Dashboard")
st.text("Welcome to the Sales Dashboard! Here you can analyze sales data and visualize trends.")
selected_month = st.selectbox("Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
sales_data = {
    "January": 1000,
    "February": 1500,
    "March": 2000,
    "April": 2500,
    "May": 3000,
    "June": 3500,
    "July": 4000,
    "August": 4500,
    "September": 5000,
    "October": 5500,
    "November": 6000,
    "December": 6500
}
st.write(f"Sales for {selected_month}: {sales_data[selected_month]} INR")
st.bar_chart(list(sales_data.values()), x_label="Month", y_label="Sales (INR)")