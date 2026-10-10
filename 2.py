
import numpy as np

# Create a matrix
A = np.array([[4, 2],
              [2, 3]])

# Covariance Analysis
data = np.array([[2, 4, 6],
                 [1, 3, 5]])

cov = np.cov(data)

print("COVARIANCE MATRIX:")
print(cov)

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEIGENVALUES:")
print(eigenvalues)

print("\nEIGENVECTORS:")
print(eigenvectors)
