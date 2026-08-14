import numpy as np 
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
matrix=np.array(m)
rank=np.linalg.matrix_rank(matrix)

print("rank of matrix:",rank)


