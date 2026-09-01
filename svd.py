import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
           
print("Enter the matrix row by row:")
A = []

for i in range(rows):
    row = list(map(float, input().split()))
    A.append(row)

A = np.array(A)


U, S, Vt = np.linalg.svd(A, full_matrices=False)

Sigma = np.zeros((rows, cols))
np.fill_diagonal(Sigma, S)

print("\nMatrix A:")
print(A)

print("\nU:")
print(U)

print("\nSingular values:")
print(S)

print("\nSigma:")
print(Sigma)

print("\nV^T:")
print(Vt)


print("\nVerification:")
print(np.allclose(A, U @ Sigma @ Vt))
