r=int(input("enter number of rows:"))
c=int(input("enter number of columns"))
m=[]
print("enter matrix elements:")
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input(f"element [{i}][{j}] : ")))
    m.append(row)
print("\n original matrix:")
for row in m:
    print(row)
print("\n transpose of matrix:")
for j in range(c):
    for i in range(r):
        print(m[i][j], end=" ")
    print()

