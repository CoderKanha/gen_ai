import streamlit as st

product_name = st.sidebar.text_input("Enter product name")
category = st.sidebar.selectbox(
    "Select Product Category",
    ("Electronics", "Clothing", "Home & Kitchen", "Books")
)
price = st.sidebar.number_input("Enter Product Price")
if st.sidebar.button("Add Product"):
    st.success(f"Product '{product_name}' added successfully!")
    st.write(f"Category: {category}")
    st.write(f"Price: {price} INR")