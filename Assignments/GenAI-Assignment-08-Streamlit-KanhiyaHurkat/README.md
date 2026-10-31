# Streamlit Practice Apps

A collection of four small [Streamlit](https://streamlit.io/) apps that demonstrate common widgets and layout features: text input, buttons, sliders, select boxes, the sidebar, tables, and charts.

## Project Structure

```
.
├── app_basic.py       # Greeting app
├── app_discount.py    # Discount calculator
├── app_product.py     # Product entry form in the sidebar
└── app_dashboard.py   # Monthly sales dashboard
```

## Requirements

- Python 3.8+
- Streamlit (a recent version is recommended, since the dashboard uses the `x_label` and `y_label` options of `st.bar_chart`)

Install Streamlit:

```bash
pip install streamlit
```

## Running an App

Run any app from the project folder:

```bash
streamlit run app_basic.py
```

Streamlit opens the app in your browser, usually at `http://localhost:8501`.

---

## 1. Greeting App (`app_basic.py`)

A minimal app that greets the user by name.

- Shows the title **Welcome to Streamlit!**
- Takes the user's name with `st.text_input`
- Clicking **Greet Me** displays `Hello, <name>!`

**Widgets used:** `st.title`, `st.text_input`, `st.button`, `st.write`

---

## 2. Discount Calculator (`app_discount.py`)

Calculates the price of a product after a percentage discount.

- **Enter Product Price**: text box for the original price
- **Select Discount Percentage**: slider from 0 to 50
- **Calculate Discount**: shows the discounted price in INR as a success message, followed by a table comparing the price before and after the discount

Formula: `discounted_price = price - (price * discount_percentage / 100)`

**Example:** a price of `100` with a `10%` discount gives a discounted price of `90.00 INR`.

**Widgets used:** `st.text_input`, `st.slider`, `st.button`, `st.success`, `st.table`

---

## 3. Product Entry Form (`app_product.py`)

A form in the sidebar for adding a product.

- **Enter product name**: text box
- **Select Product Category**: Electronics, Clothing, Home & Kitchen, or Books
- **Enter Product Price**: number input
- **Add Product**: shows a success message and displays the category and price (in INR) in the main area

**Widgets used:** `st.sidebar.text_input`, `st.sidebar.selectbox`, `st.sidebar.number_input`, `st.sidebar.button`, `st.success`, `st.write`

---

## 4. Sales Dashboard (`app_dashboard.py`)

A simple dashboard showing monthly sales.

- Shows the title **Sales Dashboard** with a short welcome text
- A **Month** select box (January to December)
- Displays the sales figure in INR for the selected month
- Shows a bar chart of sales for all twelve months

Sales data is hard-coded and increases from 1000 INR in January to 6500 INR in December.

**Widgets used:** `st.title`, `st.text`, `st.selectbox`, `st.write`, `st.bar_chart`

---

## Notes

- In `app_discount.py`, clicking **Calculate Discount** with an empty or non-numeric price raises a `ValueError`. Wrapping the `float()` conversion in a `try`/`except` and showing `st.error(...)` would handle this gracefully.
- In `app_dashboard.py`, the chart is built from a plain list of values, so the x-axis shows positions (0 to 11) rather than month names. Passing a dictionary or a DataFrame with month labels would show the names.

## Concepts Covered

- Building interactive web apps with Streamlit
- Input widgets: text input, number input, slider, select box, button
- Layout with the sidebar
- Displaying output with `st.write`, `st.success`, and `st.table`
- Data visualization with `st.bar_chart`