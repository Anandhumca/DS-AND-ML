import pandas as pd
import matplotlib.pyplot as plt

# Create student dataset
data = {
    "Name": ["Anu", "Arun", "Rahul", "Meera", "Akhil",
             "Amal", "Neha", "Vishnu", "Diya", "Riya"],

    "Department": ["MCA", "MCA", "BCA", "BCA", "MCA",
                   "BCA", "MCA", "BCA", "MCA", "BCA"],

    "Marks": [85, 72, 90, 65, 78, 88, None, 95, 70, 82]
}

df = pd.DataFrame(data)


# a) Display first 5 records and total number of students
print("First 5 records:")
print(df.head())

print("\nTotal number of students:")
print(len(df))


# b) Display count of students in each department
print("\nCount of students in each department:")
print(df["Department"].value_counts())


# c) Find students who scored more than 75 marks
print("\nStudents who scored more than 75 marks:")
print(df[df["Marks"] > 75])


# d) Fill missing marks with average marks of the class
average_marks = df["Marks"].mean()

df["Marks"] = df["Marks"].fillna(average_marks)

print("\nData after filling missing marks:")
print(df)


# e) Add a new column "Grade" based on marks
def find_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

df["Grade"] = df["Marks"].apply(find_grade)

print("\nData with Grade:")
print(df)


# f) Display department-wise average marks
print("\nDepartment-wise average marks:")
print(df.groupby("Department")["Marks"].mean())


# g) Plot a bar chart showing number of students per department
department_count = df["Department"].value_counts()

department_count.plot(kind="bar")

plt.title("Number of Students per Department")
plt.xlabel("Department")
plt.ylabel("Number of Students")

plt.show()


# h) Export students with marks greater than or equal to 90
students_90 = df[df["Marks"] >= 90]

students_90.to_csv("students_90_and_above.csv", index=False)

print("\nStudents with marks greater than or equal to 90:")
print(students_90)

print("\nData exported successfully to students_90_and_above.csv")
