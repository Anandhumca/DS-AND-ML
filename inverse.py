import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

if rows != cols:
    print("Matrix inverse is possible only for a square matrix.")
else:
    matrix = []

    print("Enter the matrix elements row by row:")

    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)

    matrix = np.array(matrix)

    
    if np.linalg.det(matrix) == 0:
        print("Inverse does not exist because the matrix is singular.")
    else:
        inverse = np.linalg.inv(matrix)

        print("\nOriginal Matrix:")
        print(matrix)

        print("\nInverse Matrix:")
        print(inverse)
