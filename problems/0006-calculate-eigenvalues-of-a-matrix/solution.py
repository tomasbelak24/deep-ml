import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	M = np.array(matrix)
	determinant = M[0][0] * M[1][1] - M[0][1] * M[1][0]
	eigenvalues = np.roots([1, -np.trace(M), determinant])
	return eigenvalues