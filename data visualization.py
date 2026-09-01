
import matplotlib.pyplot as plt
import numpy as np

# Sample data
students = ["A", "B", "C", "D", "E"]
marks = [75, 85, 60, 90, 70]

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 170, 140, 200, 220]

ages = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
heights = [160, 165, 170, 172, 175, 178, 180, 182, 185, 188]

# Create figure
plt.figure(figsize=(14, 12))


# 1. BAR CHART
# ------------------------------------------------
plt.subplot(3, 3, 1)
plt.bar(students, marks, color="skyblue")
plt.title("Bar Chart - Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")


# 2. BOX PLOT
# ------------------------------------------------
plt.subplot(3, 3, 2)
plt.boxplot(marks)
plt.title("Box Plot - Marks")
plt.ylabel("Marks")


# 3. BUBBLE CHART
# ------------------------------------------------
plt.subplot(3, 3, 3)

x = [10, 20, 30, 40, 50]
y = [15, 25, 20, 35, 40]
sizes = [100, 300, 500, 700, 1000]

plt.scatter(x, y, s=sizes, alpha=0.5,
            color="purple", edgecolors="black")
plt.title("Bubble Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")


# 4. LINE CHART
# ------------------------------------------------
plt.subplot(3, 3, 4)
plt.plot(months, sales, marker="o",
         color="green", linewidth=2)
plt.title("Line Chart - Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")


# 5. HISTOGRAM
# ------------------------------------------------
plt.subplot(3, 3, 5)
plt.hist(marks, bins=5, color="orange",
         edgecolor="black")
plt.title("Histogram - Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")


# 6. SCATTER PLOT
# ------------------------------------------------
plt.subplot(3, 3, 6)
plt.scatter(ages, heights, color="red")
plt.title("Scatter Plot - Age vs Height")
plt.xlabel("Age")
plt.ylabel("Height (cm)")


# 7. PIE CHART

plt.subplot(3, 3, 7)

subjects = ["Maths", "Science", "English", "Computer"]
values = [30, 25, 20, 25]

plt.pie(values,
        labels=subjects,
        autopct="%1.1f%%",
        startangle=90)
plt.title("Pie Chart - Subject Distribution")

# Adjust layout
plt.tight_layout()

# Display all charts
plt.show()


