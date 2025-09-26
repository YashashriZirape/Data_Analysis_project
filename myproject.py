import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Excel file 
df = pd.read_excel('Project\\Project\\bank_detailes2.xlsx')
print(df)
# ---------------------------
# 2. Data Cleaning
# ---------------------------

print("Missing values:\n", df.isnull().sum())

# Fill missing values with appropriate defaults
df["salary"] = df["salary"].fillna(0)
df["status"] = df["status"].fillna("Unknown")
df["email"] = df["email"].fillna("noemail@unknown.com")
df = df.fillna("N/A")  # General fallback

# Remove duplicate rows
df = df.drop_duplicates()

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert salary to numeric
df["salary"] = pd.to_numeric(df["salary"], errors="coerce").fillna(0)

# ---------------------------
# 3. Data Analysis
# ---------------------------

print("\nBasic Info:")
print("Total entries:", len(df))
print("Unique countries:", df["country"].nunique())
print("Gender distribution:\n", df["gender"].value_counts())

print("\nSalary Stats:")
print("Average salary:", df["salary"].mean())
print("Max salary:", df["salary"].max())
print("Min salary:", df["salary"].min())

print("\nBank Status Counts:")
print(df["status"].value_counts())

print("\nTop States by Count:")
print(df["state"].value_counts().head())

print("\nTop Districts by Count:")
print(df["district"].value_counts().head())

print("\nTop villeges by Count:")
print(df["village"].value_counts().head())
# ---------------------------
# 4. Visualization
# ---------------------------

# Bar chart - Gender distribution
df["gender"].value_counts().plot(kind="bar", title="Gender Distribution", color="skyblue")
plt.ylabel("Count")
plt.savefig("gender_distribution.png")
plt.show()

# Histogram - Salary distribution
df["salary"].plot(kind="hist", bins=10, title="Salary Distribution", color="orange")
plt.xlabel("Salary")
plt.savefig("salary_distribution.png")
plt.show()

# Pie chart - Bank Status
df["status"].value_counts().plot(kind="pie", autopct="%1.1f%%", title="Bank Status")
plt.ylabel("")
plt.savefig("bank_status_pie.png")
plt.show()

# Bar chart - Gender distribution
df["district"].value_counts().plot(kind="bar", title="villege Distribution", color="skyblue")
plt.ylabel("village")
plt.savefig("villege_distribution.png")
plt.show()
# ---------------------------
# 5. Optional - Save Cleaned Data
# ---------------------------
df.to_excel("cleaned_dataset.xlsx", index=False)
df