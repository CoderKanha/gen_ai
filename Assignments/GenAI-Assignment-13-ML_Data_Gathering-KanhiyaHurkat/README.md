# Machine Learning Task: Data Loading, Cleaning & Visualization

A Jupyter notebook (`machine_learning_task_1.ipynb`) covering the early stages of a data-science workflow with **pandas**, **NumPy**, **scikit-learn**, **Matplotlib** and **Seaborn**: loading data from several sources, understanding and cleaning it, preparing basic features, and exploring it through univariate and bivariate visualizations.

## Table of Contents

- [Tasks Covered](#tasks-covered)
- [Datasets](#datasets)
- [Requirements](#requirements)
- [Setup & Usage](#setup--usage)
- [Task Details](#task-details)
- [Key Insights](#key-insights)
- [Notes](#notes)

## Tasks Covered

| # | Task | Summary |
|---|------|---------|
| 1 | Load data from CSV | Load and inspect the International Education Costs dataset |
| 2 | Load data from JSON | Read JSON with the `json` module, `pd.read_json()`, and a URL |
| 3 | Load data from SQL | Create and query a SQLite database with `sqlite3` |
| 4 | API mini project (TMDB) | Fetch popular and top-rated movies from the TMDB API and save to CSV |
| 5 | Understanding the data | Shape, dtypes, missing values, duplicates, unique counts |
| 6 | Data cleaning | Handle missing values, duplicates, column names and data types |
| 7 | Feature preparation (basic) | Create a new feature and encode categorical columns |
| 8 | Univariate analysis | Single-variable plots on the social media dataset |
| 9 | Bivariate analysis | Two-variable (and multi-variable) plots on the social media dataset |
| 10 | Insights | Observations drawn from the visualizations |

## Datasets

| File | Used In | Description |
|------|---------|-------------|
| `International_Education_Costs.csv` | Tasks 1, 5, 6, 7 | 907 rows × 12 columns of tuition, rent, visa, insurance and living costs by university and program |
| `product.json` | Task 2 | 10 sample products (name, category, brand, price, quantity, rating, stock status) |
| `sample.db` | Task 3 | SQLite database created by the notebook (`employees` table) |
| `social_media_impact_on_life.csv` | Tasks 8, 9 | About 4,500 student records on social media usage, sleep and mental health |
| `tmdb_movies.csv`, `tmdb_top_rated_movies.csv` | Task 4 | Output files generated from the TMDB API calls |

The three input files (`International_Education_Costs.csv`, `product.json`, `social_media_impact_on_life.csv`) must be in the same directory as the notebook.

### International Education Costs: columns

`Country`, `City`, `University`, `Program`, `Level` (Bachelor / Master / PhD), `Duration_Years`, `Tuition_USD`, `Living_Cost_Index`, `Rent_USD`, `Visa_Fee_USD`, `Insurance_USD`, `Exchange_Rate`

### Social media dataset: columns used

`Age`, `Gender`, `Academic_Level`, `Primary_Platform`, `Daily_Usage_Hours`, `Weekend_Extra_Hours`, `Device_Type`, `Sleep_Duration_Hours`, `Sleep_Quality_Score`, `Mental_Health_Index`, `Perceived_Stress_Score`, `Academic_Performance_GPA`, `Social_Comparison_Frequency`, `Late_Night_Usage`, `Overall_Impact`

## Requirements

- Python 3.x (the notebook was run on a Python 3.14 kernel)
- Jupyter Notebook, JupyterLab, or VS Code with the Jupyter extension
- Libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `requests`
- Standard library: `json`, `sqlite3`

## Setup & Usage

```bash
# 1. Get the project files
# 2. (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn requests jupyter

# 4. Place the dataset files next to the notebook, then launch
jupyter notebook machine_learning_task_1.ipynb
```

For Task 4, replace the `<api_key>` placeholder in the TMDB URLs with your own key from [themoviedb.org](https://www.themoviedb.org/settings/api). Avoid committing a real key to version control; consider reading it from an environment variable instead.

## Task Details

### Task 1: Load Data from CSV
Loads the education-costs CSV with `pd.read_csv()` and inspects it using `shape`, `columns`, `head()`, `tail()`, `sample()`, `info()`, `describe()`, `dtypes`, `isna().sum()`, `unique()`, `dropna()`, `size`, `value_counts()` and conditional filtering (e.g. all programs in India).

### Task 2: Load Data from JSON
Three approaches:
1. `json.load()` on an opened file, then `pd.DataFrame(data)`
2. `pd.read_json("product.json")`
3. `pd.read_json(<url>)` against the JSONPlaceholder `/posts` endpoint

### Task 3: Load Data from SQL
Creates a SQLite database with an `employees` table (`id`, `name`, `department`, `salary`), inserts five sample records, and loads them into a DataFrame with `pd.read_sql_query()`.

### Task 4: API Mini Project (TMDB)
Calls the TMDB API with `requests`, flattens the JSON with `pd.json_normalize()`, keeps `title`, `release_date`, `vote_average`, `popularity` and `vote_count`, and saves the result to CSV. An optional step does the same for top-rated movies.

### Task 5: Understanding the Data
- Shape: **907 rows × 12 columns**
- **Numerical columns:** `Duration_Years`, `Tuition_USD`, `Living_Cost_Index`, `Rent_USD`, `Visa_Fee_USD`, `Insurance_USD`, `Exchange_Rate`
- **Categorical columns:** `Country`, `City`, `University`, `Program`, `Level`
- No missing values and no duplicate rows
- Unique counts include 71 countries, 622 universities and 92 programs

### Task 6: Data Cleaning
- **Missing values:** randomly masks 10% of a copy of the data (`df_missing`, seed 42), then imputes with the mode for most categorical and discrete columns (`"Unknown"` for `Program` and `Level`) and the median for continuous numeric columns
- **Duplicates:** checked and removed with `drop_duplicates()`
- **Column names:** renamed to lowercase snake_case (e.g. `Tuition_USD` → `tuition_usd`)
- **Data types:** categorical columns converted to `category`, numerics downcast to `int32` / `float32`, reducing memory from about 135.6 KB to about 60 KB

### Task 7: Feature Preparation (Basic)
- New feature: `total_cost_usd = tuition_usd + rent_usd`
- `OneHotEncoder` on nominal columns (`country`, `city`, `university`, `program`)
- `OrdinalEncoder` on `level` with order Bachelor < Master < PhD
- Split into feature columns (all but the last) and target (`total_cost_usd`)

### Task 8: Univariate Analysis
Uses `social_media_impact_on_life.csv`. Missing `Perceived_Stress_Score` values are filled with the median and `Academic_Performance_GPA` with the mean.

| Library | Plots |
|---------|-------|
| Seaborn | Histogram with KDE (sleep quality), count plot (overall impact), box plot (GPA), KDE plot and rug plot (mental health index), violin plot (stress score by gender), density plot via `displot` (GPA) |
| Matplotlib | Histogram (sleep quality), pie chart (social comparison frequency) |

### Task 9: Bivariate Analysis
| Library | Plots |
|---------|-------|
| Matplotlib | Scatter (age vs. weekend usage), line chart (total usage by age), bar chart (usage per platform), horizontal bar chart (weekend usage per platform), grouped bar chart and stacked bar chart (daily usage per platform by gender) |
| Seaborn | Scatter (sleep duration vs. sleep quality), heatmap (mean mental health index by device type and age), box plot (age by gender), relational plots (line and scatter, colored by gender), line plot and faceted line plot (usage by age), pair plot, violin plot (GPA by gender), joint plot (academic level vs. GPA), count plot (late-night usage by gender), dodged histogram (sleep quality by gender) |

## Key Insights

1. Users aged 18 have the highest total daily social media usage (roughly 5,500 hours combined).
2. Instagram is the most-used platform, followed by TikTok and YouTube.
3. Most users in the dataset are female.
4. Platforms are mostly used at night.
5. Late-night usage appears linked to poorer sleep, with most users reporting a sleep quality score of 3.

## Notes

- `Exchange_Rate` ranges from 0.15 to 42,150 because it is local currency per USD, so it should be scaled or handled carefully before modelling.
- `total_cost_usd` is built from `tuition_usd` and `rent_usd`, which both remain in the feature set, so a model trained as set up in Task 7 would leak the target.
- The missing-value imputation in Task 6 is demonstrated on a copy (`df_missing`); the main `df` already has no missing values.