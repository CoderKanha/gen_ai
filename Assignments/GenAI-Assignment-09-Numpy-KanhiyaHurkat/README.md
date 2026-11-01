# NumPy Practice

A set of seven Python programs that introduce [NumPy](https://numpy.org/): creating arrays, array arithmetic, mathematical functions, aggregate operations, statistics, percentiles, and a small sales analysis.

## Project Structure

```
.
├── task1_1d8da2.py   # Array creation, shape, and data type
├── task2_c53f0d.py   # Arithmetic operations on arrays
├── task3_8786e0.py   # Mathematical functions
├── task4_f419f2.py   # Aggregate operations on a 2D array
├── task5_d38c18.py   # Statistical operations on marks
├── task6_1.py        # Sorting and percentiles
└── task7_1.py        # Weekly sales analysis
```

## Requirements

- Python 3.8+
- NumPy

Install NumPy:

```bash
pip install numpy
```

## Running a Task

Run any task from the project folder:

```bash
python task1_1d8da2.py
```

---

## Task 1: Array Creation, Shape, and Data Type (`task1_1d8da2.py`)

Creates arrays in three different ways and inspects their `shape` and `dtype`.

| Array | Created with | Contents |
|-------|--------------|----------|
| One-dimensional | `np.arange(1, 11)` | 1 to 10 |
| Two-dimensional | `np.arange(1, 10).reshape(3, 3)` | 1 to 9 as a 3x3 matrix |
| Dummy array | `np.array([10, 20, 30, 40, 50])` | Converted from a Python list |

**Output**

```
Shape of one-dimensional array: (10,)
Shape of two-dimensional array: (3, 3)
Shape of dummy array: (5,)
Data type of one-dimensional array: int64
Data type of two-dimensional array: int64
Data type of dummy array: int64
```

> The default integer type depends on your platform and NumPy version, so you may see `int32` instead of `int64`.

---

## Task 2: Arithmetic Operations (`task2_c53f0d.py`)

Performs element-wise arithmetic on `[10, 20, 30, 40]` and `[1, 2, 3, 4]`, first with operators and then with the equivalent NumPy functions.

| Operation | Operator | NumPy function |
|-----------|----------|----------------|
| Addition | `+` | `np.add` |
| Subtraction | `-` | `np.subtract` |
| Multiplication | `*` | `np.multiply` |
| Division | `/` | `np.divide` |
| Square | `** 2` | `np.square` |

**Output** (the operator and function versions give identical results)

```
Addition: [11 22 33 44]
Subtraction: [ 9 18 27 36]
Multiplication: [ 10  40  90 160]
Division: [10. 10. 10. 10.]
Square: [ 100  400  900 1600]
```

---

## Task 3: Mathematical Functions (`task3_8786e0.py`)

Applies common mathematical functions to the array `[2, 4, 6, 8, 10]`.

| Function | Description |
|----------|-------------|
| `np.sqrt` | Square root of each element |
| `np.exp` | Exponential (e^x) of each element |
| `np.log` | Natural logarithm of each element |
| `np.sum` | Sum of all elements |
| `np.cumsum` | Running (cumulative) sum |

**Output**

```
Square Root: [1.41421356 2.         2.44948974 2.82842712 3.16227766]
Exponential: [7.38905610e+00 5.45981500e+01 4.03428793e+02 2.98095799e+03
 2.20264658e+04]
Logarithm: [0.69314718 1.38629436 1.79175947 2.07944154 2.30258509]
Sum of Elements: 30
Cumulative Sum: [ 2  6 12 20 30]
```

---

## Task 4: Aggregate Operations (`task4_f419f2.py`)

Works with a 3x3 array and uses the `axis` argument to aggregate along rows or columns.

```
[[10 20 30]
 [40 50 60]
 [70 80 90]]
```

- `axis=1` aggregates across each **row**
- `axis=0` aggregates down each **column**
- No axis aggregates the whole array

**Output**

```
Row-wise Sum: [ 60 150 240]
Column-wise Sum: [120 150 180]
Minimum Value: 10
Maximum Value: 90
Mean Value: 50.0
Row-wise Minimum: [10 40 70]
Row-wise Maximum: [30 60 90]
Column-wise Minimum: [10 20 30]
Column-wise Maximum: [70 80 90]
```

---

## Task 5: Statistical Operations (`task5_d38c18.py`)

Calculates descriptive statistics for student marks: `[78, 85, 90, 66, 72, 88, 95, 60]`.

| Function | Description |
|----------|-------------|
| `np.mean` | Average |
| `np.median` | Middle value |
| `np.var` | Variance |
| `np.std` | Standard deviation |
| `np.min` / `np.max` | Lowest and highest marks |
| `np.ptp` | Range (max minus min) |

**Output**

```
Mean Marks: 79.25
Median Marks: 81.5
Variance Marks: 134.1875
Standard Deviation Marks: 11.583932838203095
Minimum Marks: 60
Maximum Marks: 95
Range of Marks: 35
```

---

## Task 6: Percentiles and Sorting (`task6_1.py`)

Uses the same marks array to sort the data, find percentiles, and count how many students scored above the average.

- `np.sort` returns the marks in ascending order
- `np.percentile` finds the 25th, 50th, and 75th percentiles
- `np.sum(marks > np.mean(marks))` counts the marks above the mean (a boolean comparison where `True` counts as 1)

**Output**

```
Sorted Marks: [60 66 72 78 85 88 90 95]
25th Percentile: 70.5
50th Percentile: 81.5
75th Percentile: 88.5
Number of Students Above Average: 79.25 4
```

The last line prints the average (`79.25`) followed by the count (`4`). The 50th percentile equals the median from Task 5.

---

## Task 7: Weekly Sales Analysis (`task7_1.py`)

Analyzes seven days of sales: `[1200, 1500, 900, 2000, 1800, 1700, 1600]`.

| Metric | Function |
|--------|----------|
| Total weekly sales | `np.sum` |
| Average daily sales | `np.mean` |
| Highest and lowest sales | `np.max`, `np.min` |
| Standard deviation | `np.std` |
| Days above average | `np.where(sales > average)` |

**Output**

```
Total Weekly Sales: 10700
Average Daily Sales: 1528.5714285714287
Highest Sales: 2000
Lowest Sales: 900
Standard Deviation of Sales: 345.2298849598449
Days Above Average Sales: [3 4 5 6]
```

`np.where` returns array indices, which start at 0. So `[3 4 5 6]` means the 4th to 7th days of the week were above average.

---

## Concepts Covered

- Creating arrays with `np.array`, `np.arange`, and `reshape`
- Array attributes: `shape` and `dtype`
- Element-wise arithmetic and NumPy's equivalent functions
- Mathematical functions: `sqrt`, `exp`, `log`, `cumsum`
- Aggregation along an axis
- Descriptive statistics: mean, median, variance, standard deviation, range
- Percentiles and sorting
- Boolean comparison and `np.where` for filtering