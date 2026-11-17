# Feature Engineering & Preprocessing Pipelines

A hands-on Jupyter notebook (`feature_engineering_task.ipynb`) covering the core feature engineering workflow in Python: creating new features, encoding, scaling, and building reusable scikit-learn pipelines. It finishes with two end-to-end models (regression and classification) and a short written reflection on why pipelines matter.

## Table of Contents

- [Datasets](#datasets)
- [Notebook Structure](#notebook-structure)
- [Key Results](#key-results)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Notes and Known Issues](#notes-and-known-issues)

## Datasets

Two CSV files are expected in the same folder as the notebook (they are **not** included in this repository):

| File | Rows | Used in | Description |
|---|---|---|---|
| `retail_sales_dataset.csv` | 2,500 | Tasks 1-7 | Retail orders with date, customer age, product, category, quantity, unit price, discount, unit cost, city, sales channel, payment method, and a free-text customer review. |
| `electronic_store_sample_data.csv` | 15,132 | Task 8 | Electronics store orders with customer demographics, product type, rating, order status, payment method, prices, quantity, purchase date, and shipping type. |

## Notebook Structure

### Setup
Loads `retail_sales_dataset.csv` with pandas and inspects its structure.

### Task 1 - Creating New Features
Converts `Order_Date` to datetime and derives business metrics:

- `Total_Value` = Quantity × Unit_Price
- `Revenue` = Total_Value × (1 − Discount_Rate)
- `Total_Cost` = Quantity × Unit_Cost
- `Profit` = Revenue − Total_Cost

### Task 2 - Handling Date and Text Features
- Extracts `Order_Year`, `Order_Month`, and `Order_Day` from the order date.
- Creates text features from `Customer_Review`: character length (`Review_Lenth`) and word count (`Review_Word_Count`).
- Selects the columns needed for modelling and casts them to memory-efficient dtypes (`int32`, `category`).

### Task 3 - One-Hot Encoding
Encodes all categorical columns using `pd.get_dummies`.

### Task 4 - ColumnTransformer
Builds a `ColumnTransformer` that one-hot encodes categorical columns (`OneHotEncoder` with `handle_unknown="ignore"`) and passes numeric columns through unchanged. The transformed output has 60 columns.

### Task 5 - Standardization
Applies `StandardScaler` to the numeric columns (zero mean, unit variance).

### Task 6 - Normalization (MinMax Scaler)
Applies `MinMaxScaler` to scale numeric columns to the 0-1 range, then builds a side-by-side comparison table of the original, standardized, and min-max-scaled statistics.

### Task 7 - Preprocessing Pipeline
Builds a reusable preprocessing `ColumnTransformer` with separate sub-pipelines:

| Column type | Steps |
|---|---|
| Numerical | `SimpleImputer(mean)` → `StandardScaler` |
| Nominal | `SimpleImputer(most_frequent)` → `OneHotEncoder` |
| Ordinal | None present in this dataset |

### Task 8 - Full scikit-learn Pipeline
Uses the electronics store dataset and combines preprocessing and a model in a single `Pipeline`.

**Feature handling**

| Type | Columns | Processing |
|---|---|---|
| Numeric | Age, Rating, Unit Price, Quantity, Purchase Year, Purchase Month | Impute (mean) → Scale |
| Ordinal | Order Status (`Cancelled` < `Completed`) | Impute → `OrdinalEncoder` → Scale |
| Nominal | Gender, Loyalty Member, Product Type, Payment Method, Shipping Type | Impute → `OneHotEncoder` → Scale |

**Models**

1. **Linear Regression** - predicts `Total Price`; evaluated with MAE, MSE, RMSE, and R².
2. **Logistic Regression** - predicts `Rating`; evaluated with accuracy.

Both use an 80/20 train/test split.

### Task 9 - Pipeline Benefits
A written discussion covering why pipelines matter, which problems they solve (notably data leakage), and a comparison of manual vs. pipeline-based preprocessing.

## Key Results

Results from the executed notebook (the splits are not seeded, so numbers will vary slightly between runs):

| Model | Target | Metric | Value |
|---|---|---|---|
| Linear Regression | Total Price | R² | ≈ 0.877 |
| | | MAE | ≈ 666.05 |
| | | RMSE | ≈ 891.04 |
| Logistic Regression | Rating | Accuracy | ≈ 0.574 |

## Requirements

- Python 3.10+ (the notebook was run on a recent Python 3 kernel)
- pandas (a recent version; the notebook output shows the newer `str` dtype)
- scikit-learn (uses `sparse_output` in `OneHotEncoder` and `root_mean_squared_error`, so **1.2+** is required)
- Jupyter Notebook or JupyterLab

## Getting Started

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd <your-repo-folder>

# 2. (Optional) create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install pandas scikit-learn notebook

# 4. Place the datasets next to the notebook
#    - retail_sales_dataset.csv
#    - electronic_store_sample_data.csv

# 5. Launch the notebook
jupyter notebook feature_engineering_task.ipynb
```

Then run the cells from top to bottom.

## Project Structure

```
.
├── feature_engineering_task.ipynb
├── retail_sales_dataset.csv            # not included - add your own copy
├── electronic_store_sample_data.csv    # not included - add your own copy
└── README.md
```

## Notes and Known Issues

- **Typo in column name:** `Review_Lenth` should be `Review_Length`. It is kept as-is to match the notebook.
- **Unused features:** `Order_Day`, `Review_Lenth`, and `Review_Word_Count` are created in Task 2 but dropped when selecting `final_retail_sales_df`.
- **`SettingWithCopyWarning`:** the dtype conversions in Task 8's prep step are applied to a sliced DataFrame; using `.copy()` when slicing avoids the warning.
- **Reproducibility:** `train_test_split` is called without `random_state`; set one (e.g. `random_state=42`) for repeatable results.
- **Scaled one-hot features:** in Task 8, one-hot encoded columns are passed through `StandardScaler`. This works, but it is optional and makes coefficients harder to interpret.
- **Logistic Regression on Rating:** `Total Price` is included as a feature while `Rating` is the target. Check this makes sense for your use case, and consider reporting more than accuracy if the classes are imbalanced.
- **Possible data leakage in the regression model:** `Total Price` is likely derived from `Unit Price × Quantity`, both of which are features, which helps explain the high R².

## License

Add a license of your choice (e.g. MIT) before publishing.