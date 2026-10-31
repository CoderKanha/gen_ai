import streamlit as st

product_price = st.text_input("Enter Product Price", key="price")
discount_percentage = st.slider("Select Discount Percentage", 0, 50, key="discount")
if st.button("Calculate Discount"):
    price = float(product_price)
    discounted_price = price - (price * discount_percentage / 100)
    st.success(f"Discounted Price: {discounted_price: .2f}INR")
    st.table({"Price Before Discount": [price], "Price After Discount": [discounted_price]})