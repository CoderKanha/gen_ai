import pandas as pd

marks = [78, 85, 90, 66, 72]

#--------------------------------------------------------------------
# Task 1: Pandas Series Basics
#--------------------------------------------------------------------
marks_series = pd.Series(marks)

# Print Series value
print("Marks Series:", marks_series.values)
# Print series index
print("Marks Series Index:", marks_series.index)
# Print series data type
print("Marks Series Data Type:", marks_series.dtype)
# Accessing first element of the series
print("First Element of Marks Series:", marks_series[0])
# Accessing last two elements of the series
print("Last Two Elements of Marks Series:\n", marks_series[-2:])


#--------------------------------------------------------------------
# Task 2: Mathamatical Operations on Series
#--------------------------------------------------------------------

# Add 5 grace marks to each student's score
grace_marks_series = marks_series + 5
print("Grace Marks Series:", grace_marks_series.values)

# Subtract 2 marks from each student's score
deducted_marks_series = marks_series - 2
print("Deducted Marks Series:", deducted_marks_series.values)

# Multiply all marks by 1.05
multiplied_marks_series = marks_series * 1.05
print("Multiplied Marks Series:", multiplied_marks_series.values)

# Divide all marks by 2
divided_marks_series = marks_series / 2
print("Divided Marks Series:", divided_marks_series.values)


#--------------------------------------------------------------------
# Task 3: Python Functionalities on Series
#--------------------------------------------------------------------

# Find the maximum marks
max_marks = marks_series.max()
print("Maximum Marks:", max_marks)

# Find the minimum marks
min_marks = marks_series.min()
print("Minimum Marks:", min_marks)

# Sum of all marks
total_marks = marks_series.sum()
print("Total Marks:", total_marks)

# Mean of all marks
mean_marks = marks_series.mean()
print("Mean Marks:", mean_marks)

# Check whether all marks are greater or equal to 70
all_above_70 = marks_series.ge(70)
print("All Marks Above 70:\n", all_above_70)

# Count how many students scored passed (>= 70)
passed_students = marks_series.ge(70).sum()
print("Number of Passed Students:", passed_students)


#--------------------------------------------------------------------
# Task 4: Create a DataFrame from Series
#--------------------------------------------------------------------
students = {
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    "Marks": marks_series,
    "Subject": ["Math", "Math", "Science", "Science", "Math"]
}

# Convert the dictionary to a DataFrame
students_df = pd.DataFrame(students)
print("Students DataFrame:\n", students_df)

# Print first 3 rows of the DataFrame
print("First 3 Rows of Students DataFrame:\n", students_df.head(3))

# Print last 2 rows of the DataFrame
print("Last 2 Rows of Students DataFrame:\n", students_df.tail(2))

# Print the DataFrame shape and column names
print("DataFrame Shape:", students_df.shape)
print("DataFrame Columns:", students_df.columns)


#--------------------------------------------------------------------
# Task 5: Important dataframe functions
#--------------------------------------------------------------------

# Print students DataFrame info
print("Students DataFrame Info:", students_df.info())

# Print students DataFrame description
print("Students DataFrame Description:", students_df.describe())

# Print students DataFrame head
print("Students DataFrame Head:", students_df.head())

# Print students DataFrame tail
print("Students DataFrame Tail:", students_df.tail())

# Sort the DataFrame by Marks in descending order using index
sorted_students_df = students_df.set_index("Marks").sort_index(ascending=False)
print("Sorted Students DataFrame by Index (Descending):\n", sorted_students_df)

# Reset the index of the sorted DataFrame
reset_index_df = sorted_students_df.reset_index()
print("Reset Index DataFrame:\n", reset_index_df)


#--------------------------------------------------------------------
# Task 6: Filtering and Conditional Selection
#--------------------------------------------------------------------

# Students who scored more than 75 marks
high_scorers = students_df[students_df["Marks"] > 75]
print("Students who scored more than 75 marks:\n", high_scorers)

# Students belonging to Math subject
math_students = students_df[students_df["Subject"] == 'Math']
print("Students in the Math subject:\n", math_students)

# Students who scored above average marks
above_average_students = students_df[students_df["Marks"] > students_df["Marks"].mean()]
print("Students who scored above average marks:\n", above_average_students)

# Students who failed (scored less than 70 marks)
failed_students = students_df[students_df["Marks"] < 70]
print("Students who failed (scored less than 70 marks):\n", failed_students)


#--------------------------------------------------------------------
# Task 7: Grouping and Basic Analysis
#--------------------------------------------------------------------

# Average marks for each subject using groupby
average_marks_by_subject = students_df.groupby("Subject")["Marks"].mean()
print("Average Marks by Subject:\n", average_marks_by_subject)

# Count of students in each subject
student_count_by_subject = students_df["Subject"].value_counts()
print("Student Count by Subject:\n", student_count_by_subject)

# Maximum marks in each subject
max_marks_by_subject = students_df.groupby("Subject")["Marks"].max()
print("Maximum Marks by Subject:\n", max_marks_by_subject)


#--------------------------------------------------------------------
# Task 8: Pandas Plotting
#--------------------------------------------------------------------

# Plot graph of student name and their marks
data = students_df.set_index("Name")[["Marks"]]
x = data.index
y = data.values
data.plot(kind="bar").get_figure().savefig('studentVsMarksBarChart.png')

# Plot a line graph of marks
data.plot(kind="line").get_figure().savefig('studentVsMarksLineChart.png')

# Plot a histogram graph of marks
data.plot(kind="hist").get_figure().savefig('studentVsMarksHistChart.png')


#--------------------------------------------------------------------
# Task 9: Mini Usecase: Sales Data Analysis
#--------------------------------------------------------------------

# Create dataframs
sales = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Revenue": [1200, 1500, 900, 2000, 1800]
}
sales_df = pd.DataFrame(sales)

# Total revenue
total_revenue = sales_df["Revenue"].sum()
print("Total sales revenue:", total_revenue)

# Average daily revenue
average_daily_revenue = sales_df["Revenue"].mean()
print("Average daily revenue:", average_daily_revenue)

# Day with highest revenue
highest_revenue_day = sales_df[sales_df['Revenue'] == sales_df['Revenue'].max()]["Day"]
print(highest_revenue_day)

# Day greater than average revenue
days_above_average_revenue = sales_df[sales_df['Revenue'] > sales_df['Revenue'].mean()]["Day"]
print(days_above_average_revenue)

# Plot revenue vs. day graph
sales_df.plot(kind="bar").get_figure().savefig('revenueVsDayBarChart.png')