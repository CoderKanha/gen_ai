# Seaborn Data Visualization Practice

A Jupyter notebook (`seabornTask.ipynb`) that explores a student performance dataset using Seaborn and Matplotlib. It covers the main Seaborn plot families: relational, line, distribution, bivariate distribution, matrix, categorical, and regression plots.

## Project Structure

```
.
├── seabornTask.ipynb                       # The notebook
└── student_performance_factors_data.csv    # Dataset (not included, add it here)
```

> **Note:** The notebook reads `student_performance_factors_data.csv` from the same folder, so make sure the file is in place before running it.

## Requirements

- Python 3.8+
- Jupyter Notebook or JupyterLab
- pandas
- matplotlib
- seaborn 0.12 or newer (the notebook passes the DataFrame as the first positional argument)

Install the dependencies:

```bash
pip install pandas matplotlib seaborn notebook
```

## Running the Notebook

```bash
jupyter notebook seabornTask.ipynb
```

Then run the cells from top to bottom.

---

## Data Preparation

After loading the CSV with `pd.read_csv`, the notebook converts columns to smaller data types to reduce memory usage.

| Type | Columns |
|------|---------|
| `int8` | `Hours_Studied`, `Attendance`, `Sleep_Hours`, `Previous_Scores`, `Tutoring_Sessions`, `Physical_Activity`, `Exam_Score` |
| `category` | `Parental_Involvement`, `Access_to_Resources`, `Extracurricular_Activities`, `Motivation_Level`, `Internet_Access`, `Family_Income`, `Teacher_Quality`, `School_Type`, `Peer_Influence`, `Learning_Disabilities`, `Parental_Education_Level`, `Distance_from_Home`, `Gender` |

`student_data.sample(5)` is then used to preview a random sample of rows.

---

## Tasks

### Task 1: Relational Plot

Uses `sns.relplot` to show the relationship between two numerical columns.

| Plot | Variables | Notes |
|------|-----------|-------|
| Line | `Hours_Studied` vs `Attendance` | `kind="line"` |
| Line with hue | `Sleep_Hours` vs `Previous_Scores` | Colored by `Gender` |
| Scatter | `Sleep_Hours` vs `Previous_Scores` | `kind="scatter"`, colored by `Gender` |

### Task 2: Line Plot

| Plot | Variables | Notes |
|------|-----------|-------|
| `sns.lineplot` | `Hours_Studied` vs `Attendance` | Basic line plot |
| `sns.scatterplot` | `Hours_Studied` vs `Attendance` | `hue="Gender"`, point size by `Exam_Score` |
| `sns.relplot` with facets | `Hours_Studied` vs `Attendance` | Separate scatter plot per gender using `col="Gender"` |

### Task 3: Distribution Plots

All plots show the distribution of `Previous_Scores`.

| Plot | Function | Notes |
|------|----------|-------|
| Histogram | `sns.histplot` | Counts of scores in bins |
| KDE | `sns.kdeplot` | Smooth density curve, filled, colored by `Gender` |
| Rug | `sns.rugplot` | Tick marks for each observation |
| Histogram + KDE | `sns.histplot(kde=True)` | Histogram with a density curve overlaid |

### Task 4: Bivariate Distribution Plots

Both plots show how `Hours_Studied` and `Attendance` are distributed together.

| Plot | Function |
|------|----------|
| Bivariate histogram | `sns.histplot` with `x` and `y` |
| Bivariate KDE | `sns.kdeplot` with `x` and `y` |

### Task 5: Matrix Plots

| Plot | Description |
|------|-------------|
| Pair plot | `sns.pairplot` with `hue="Gender"`, showing relationships between all numerical columns |
| Heatmap | Average `Exam_Score` for each combination of `Parental_Involvement` (rows) and `Sleep_Hours` (columns), built with `pivot_table` and drawn with `sns.heatmap(annot=True)` |

### Task 6: Categorical Plots

All four plots use `Teacher_Quality` on the x-axis and include a grid.

| Plot | Function | Y variable |
|------|----------|------------|
| Bar plot | `sns.barplot` | `Sleep_Hours` (average per category) |
| Box plot | `sns.boxplot` | `Sleep_Hours` |
| Violin plot | `sns.violinplot` | `Sleep_Hours` |
| Count plot | `sns.countplot` | Number of students per category |

### Task 7: Regression Plots

Both plots fit a regression line between `Hours_Studied` and `Exam_Score`.

| Plot | Function | Notes |
|------|----------|-------|
| Regression plot | `sns.regplot` | Single regression line |
| LM plot | `sns.lmplot` | `hue="Gender"` fits a separate line for each gender |

---

## Concepts Covered

- Loading data with pandas and reducing memory with `astype("int8")` and `astype("category")`
- Figure-level functions (`relplot`, `pairplot`, `lmplot`) and axes-level functions (`lineplot`, `scatterplot`, `histplot`, etc.)
- Using `hue`, `size`, and `col` to add extra dimensions to a plot
- Univariate and bivariate distribution plots
- Reshaping data with `pivot_table` for heatmaps
- Comparing categories with bar, box, violin, and count plots
- Fitting and visualizing regression lines