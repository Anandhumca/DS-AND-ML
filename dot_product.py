r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

m1 = []
m2 = []

print("Enter first matrix elements:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input(f"Element [{i}][{j}] : ")))
    m1.append(row)

print("Enter second matrix elements:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input(f"Element [{i}][{j}] : ")))
    m2.append(row)

print("\nFirst matrix:")
for row in m1:
    print(row)

print("\nSecond matrix:")
for row in m2:
    print(row)

result = [[0] * c for i in range(r)]

for i in range(r):
    for j in range(c):
        for k in range(c):
            result[i][j] += m1[i][k] * m2[k][j]

print("\nDot product of matrices:")
for row in result:
    print(row)
