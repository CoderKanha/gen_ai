# Electronic Store Sales Analysis

This repository contains a Jupyter Notebook dedicated to analyzing and visualizing electronic store sales data. The project utilizes `pandas` for data manipulation and memory optimization, alongside `matplotlib` to generate various insightful visualizations.

## Overview

The analysis begins by loading raw sales data (`electronic_store_sample_data.csv`) and performing data type conversions to heavily optimize memory usage. It then explores the dataset through multiple plotting techniques to uncover trends in monthly sales, customer demographics, and product performance.

## Data Manipulation & Optimization
To handle the data efficiently, several preprocessing steps were taken:
*   **Memory Optimization:** Downcasted columns to `category` (Gender, Loyalty Member, Product Type, Order Status, Payment Method, Shipping Type) and `int8` (Rating, Age) to significantly reduce the DataFrame's memory footprint.
*   **Date Processing:** Converted the `Purchase Date` column to proper pandas `datetime` objects.
*   **Feature Extraction:** Extracted the month name from the purchase date into a new `Purchase Month` categorical column to facilitate time-series grouping.

## Visualizations

The notebook covers 7 primary visualization tasks:

1.  **Line Plot (Monthly Sales):** A chronological line chart tracking total sales month-by-month to identify seasonal trends.
2.  **Scatter Plot (Purchasing Strength by Age):** Maps out total purchase amounts against customer age to identify which age brackets drive the most revenue.
3.  **Bar Plots (Sales by Product Type):** Both vertical and horizontal bar charts displaying the total sales volume across different product categories.
4.  **Multi Bar Plot (Product Sales by Gender):** A grouped bar chart comparing the sales of each product type segmented by male and female customers.
5.  **Stacked Bar Plot (Product Sales by Gender):** A stacked variation of the multi-bar plot to show cumulative sales by gender while breaking down the product composition.
6.  **Histogram (Rating Distribution):** Displays the frequency distribution of customer ratings (1 to 5 stars).
7.  **Pie Chart (Product Type Distribution):** Illustrates the overall market share/percentage breakdown of each product type sold.

## Requirements
*   Python 3.x
*   Pandas
*   NumPy
*   Matplotlib