
import numpy as np

# VECTOR OPERATIONS
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print("VECTOR OPERATIONS")
print("Vector A:", A)
print("Vector B:", B)
print("Addition:", A + B)
print("Subtraction:", A - B)
print("Multiplication:", A * B)
print("Dot Product:", np.dot(A, B))
print("Scalar Multiplication:", 2 * A)
print("Magnitude:", np.linalg.norm(A))

# MATRIX OPERATIONS
X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])

print("\nMATRIX OPERATIONS")
print("Matrix X:\n", X)
print("Matrix Y:\n", Y)
print("Addition:\n", X + Y)
print("Subtraction:\n", X - Y)
print("Element-wise Multiplication:\n", X * Y)
print("Matrix Multiplication:\n", np.dot(X, Y))
print("Transpose of X:\n", X.T)
print("Determinant of X:", np.linalg.det(X))
print("Inverse of X:\n", np.linalg.inv(X))
