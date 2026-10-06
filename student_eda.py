import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create student performance dataset
data = {
    "StudentID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Gender": [
        "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male"
    ],
    "StudyHours": [
        2, 3, 4, 5, 6, 7, 3, 8, 5, 4, 6, 7
    ],
    "Attendance(%)": [
        80, 85, 90, 88, 95, 92, 78, 96, 89, 84, 93, 91
    ],
    "Marks": [
        60, 65, np.nan, 72, 78, 85,
        68, 90, np.nan, 70, 82, 88
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Add an exact duplicate row
df = pd.concat([df, df.iloc[[11]]], ignore_index=True)

# Save dataset as CSV
df.to_csv("student_performance.csv", index=False)

# Load the CSV file
df = pd.read_csv("student_performance.csv")

# Display shape
print("Shape:", df.shape)

# Display first few rows
print("\nFirst 5 rows:")
print(df.head())

# Display information
print("\nDataset Information:")
df.info()

# Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Drop duplicate row
df_clean = df.drop_duplicates()

# Fill missing Marks with the median
marks_median = df_clean["Marks"].median()
df_clean["Marks"] = df_clean["Marks"].fillna(marks_median)

# Display shape after cleaning
print("\nAfter cleaning:", df_clean.shape)

# Display cleaned data
print("\nCleaned dataset:")
print(df_clean)

# Marks Histogram
plt.figure(figsize=(7, 5))

plt.hist(
    df_clean["Marks"],
    bins=6,
    edgecolor="black"
)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")

plt.tight_layout()
plt.savefig("marks_histogram.png")
plt.close()

# Marks Boxplot
plt.figure(figsize=(7, 5))

plt.boxplot(df_clean["Marks"])

plt.ylabel("Marks")
plt.title("Marks Boxplot")

plt.tight_layout()
plt.savefig("marks_boxplot.png")
plt.close()

print("\nSaved marks_histogram.png, marks_boxplot.png")

# Scatter plot: Study Hours vs Marks
plt.figure(figsize=(7, 5))

plt.scatter(
    df_clean["StudyHours"],
    df_clean["Marks"]
)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.tight_layout()
plt.savefig("studyhours_vs_marks.png")
plt.close()

# Full numeric correlation matrix
correlation_matrix = df_clean[
    ["StudyHours", "Attendance(%)", "Marks"]
].corr()

print("\nCorrelation matrix:")
print(correlation_matrix)

print("\nSaved studyhours_vs_marks.png")
# Average Marks and Attendance by Gender
gender_summary = df_clean.groupby("Gender")[["Marks", "Attendance(%)"]].mean()

print("\nAverage Marks and Attendance by Gender:")
print(gender_summary)