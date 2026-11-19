# Core Machine Learning Algorithms: Electronic Store Dataset

A Jupyter notebook (`core_algorithm.ipynb`) that walks through eight foundational machine learning tasks using scikit-learn on an electronic store sales dataset (`electronic_store_sample_data.csv`, ~15,000 orders).

The notebook covers regression, classification, model evaluation, overfitting/underfitting, and the bias-variance tradeoff.

---

## Table of Contents

- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Tasks Overview](#tasks-overview)
- [Results Summary](#results-summary)
- [Key Observations](#key-observations)
- [Known Issues](#known-issues)

---

## Dataset

**File:** `electronic_store_sample_data.csv` (15,132 rows)

| Column | Type | Used As |
|---|---|---|
| `Age` | Numerical | Feature |
| `Rating` | Numerical | Feature |
| `Unit Price` | Numerical | Feature |
| `Quantity` | Numerical | Feature |
| `Total Price` | Numerical | Target (Task 1), Feature (Tasks 3-7) |
| `Gender` | Categorical | Feature |
| `Loyalty Member` | Categorical | Feature |
| `Product Type` | Categorical | Feature |
| `Shipping Type` | Categorical | Feature |
| `Order Status` | Categorical (Completed / Cancelled) | Target (Tasks 3-7) |

The dataset has no missing values in the columns used.

## Project Structure

```
.
├── core_algorithm.ipynb                 # Main notebook (Tasks 1-8)
├── electronic_store_sample_data.csv     # Dataset
└── README.md
```

## Requirements

- Python 3.9+
- pandas
- numpy
- matplotlib
- scikit-learn **1.4 or newer** (needed for `root_mean_squared_error`)
- Jupyter Notebook / JupyterLab

Install everything with:

```bash
pip install pandas numpy matplotlib scikit-learn jupyter
```

## Getting Started

1. Clone or download this repository.
2. Place `electronic_store_sample_data.csv` in the same folder as the notebook.
3. Launch Jupyter:
   ```bash
   jupyter notebook core_algorithm.ipynb
   ```
4. Run all cells from top to bottom. The cells depend on each other (shared variables such as `df`, `X_train`, and `y_test`), so run them in order.

---

## Tasks Overview

### Task 1: Linear Regression
Predicts **Total Price** from `Unit Price`, `Quantity`, `Age`, and `Rating` using an 80/20 train/test split. Results are visualized with an **Actual vs Predicted** scatter plot, where a red dashed diagonal marks perfect predictions.

### Task 2: Regression Evaluation Metrics
Evaluates the Task 1 model with **MAE**, **MSE**, and **RMSE**.

### Task 3: Logistic Regression
Classifies **Order Status** (Cancelled = 0, Completed = 1). Text features are converted with `pd.get_dummies`, the data is split 80/20 with stratification, and features are scaled with `StandardScaler`.

### Task 4: Naive Bayes Classifier
Trains a `GaussianNB` model on the same data and compares it with Logistic Regression.

### Task 5: K-Nearest Neighbors (KNN)
Trains KNN with 17 different values of **k** (1 to 100), plots accuracy against k, and selects the best-performing k. Categorical features are one-hot encoded and scaled, since KNN is distance-based.

### Task 6: Classification Evaluation Metrics
Compares Logistic Regression, Naive Bayes, and KNN using **Accuracy, Precision, Recall, F1-score, Classification Report,** and **Confusion Matrix**.

### Task 7: Overfitting & Underfitting
Trains three Decision Trees of different complexity and compares training vs testing accuracy:

| Model | Configuration |
|---|---|
| Underfit | `max_depth=1` |
| Balanced | `max_depth=5` |
| Overfit | `max_depth=None` (no limit) |

### Task 8: Bias & Variance (Conceptual)
Written answers covering:
1. What bias is
2. What variance is
3. How both relate to underfitting and overfitting
4. Ways to reduce overfitting

---

## Results Summary

### Regression (Tasks 1-2)

| Metric | Value |
|---|---|
| MAE | 671.37 |
| MSE | 790,748.00 |
| RMSE | 889.24 |

### Classification (Tasks 3-6)

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 0.6703 | 0.6703 | 1.00 | 0.8026 |
| Naive Bayes | 0.6703 | 0.6703 | 1.00 | 0.8026 |
| KNN (best k = 71) | 0.6700 | n/a | n/a | n/a |

**KNN accuracy by k** (selected values):

| k | 1 | 5 | 11 | 21 | 41 | 71 | 100 |
|---|---|---|---|---|---|---|---|
| Accuracy | 0.5448 | 0.5930 | 0.6234 | 0.6531 | 0.6680 | **0.6700** | 0.6693 |

### Overfitting vs Underfitting (Task 7)

| Model | Train Accuracy | Test Accuracy | Tree Depth |
|---|---|---|---|
| Underfit (`max_depth=1`) | 0.6705 | 0.6703 | 1 |
| Balanced (`max_depth=5`) | 0.6734 | 0.6683 | 5 |
| Overfit (`max_depth=None`) | 0.9756 | 0.5349 | 39 |

---

## Key Observations

- **Regression:** Total Price is largely `Unit Price × Quantity`, a multiplicative relationship, so a plain linear model fits reasonably but not perfectly. Adding an interaction feature (`Unit Price * Quantity`) would likely improve it.
- **Class imbalance:** About 67% of orders are "Completed". Logistic Regression and Naive Bayes both predict "Completed" for *every* test sample, so their 0.67 accuracy equals the majority-class baseline, with precision and recall of 0 for the "Cancelled" class.
- **KNN:** Accuracy rises as k grows (small k overfits to noise) and plateaus near 0.67, again matching the baseline.
- **Overfitting:** The unrestricted Decision Tree reaches ~97.6% training accuracy but only ~53.5% testing accuracy. This large gap is the signature of high variance. The depth-1 tree shows underfitting (high bias) with similar, low accuracy on both sets.
- **Overall:** The available features carry very little signal for predicting order cancellation. Improving on the baseline would need better features, class-imbalance handling (e.g. `class_weight="balanced"`), or different evaluation metrics focused on the minority class.

## Known Issues

- **Task 5 / Task 6:** `knn_y_pred` is computed from the *last* KNN model trained in the loop (k = 100), not the best k (71). To evaluate the best model, retrain with `KNeighborsClassifier(n_neighbors=best_k)` before predicting.
- In Task 5, the variable `scaler` is reassigned, and `X` / `X_train` are rebuilt using one-hot encoding rather than `get_dummies`, so feature columns differ slightly from Task 3.
- sklearn may print `UndefinedMetricWarning` for the "Cancelled" class because no samples are predicted as that class. Pass `zero_division=0` to the metric functions to silence it.

## License

This project is intended for educational purposes.