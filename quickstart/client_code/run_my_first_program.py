# run_my_first_program.py

import cmath
import numpy as np

def solve_quadratic(a, b, c):
    """Solves the quadratic equation ax^2 + bx + c = 0 and returns its roots."""
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    return root1, root2

def matrix_multiplication(A, B):
    """Performs matrix multiplication of two matrices A and B."""
    return np.dot(A, B)

def eigenvalues_and_eigenvectors(matrix):
    """Calculates the eigenvalues and eigenvectors of a given matrix."""
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

def main():
    # Solving a quadratic equation
    a = float(input("Enter coefficient a for the quadratic equation: "))
    b = float(input("Enter coefficient b for the quadratic equation: "))
    c = float(input("Enter coefficient c for the quadratic equation: "))
    
    root1, root2 = solve_quadratic(a, b, c)
    print(f"The roots of the quadratic equation are {root1} and {root2}")

    # Matrix multiplication
    print("Enter the elements of the first 2x2 matrix:")
    A = []
    for i in range(2):
        row = list(map(float, input().split()))
        A.append(row)
    A = np.array(A)

    print("Enter the elements of the second 2x2 matrix:")
    B = []
    for i in range(2):
        row = list(map(float, input().split()))
        B.append(row)
    B = np.array(B)

    result = matrix_multiplication(A, B)
    print("The result of matrix multiplication is:")
    print(result)

    # Eigenvalues and eigenvectors
    print("Enter the elements of a 2x2 matrix to find its eigenvalues and eigenvectors:")
    matrix = []
    for i in range(2):
        row = list(map(float, input().split()))
        matrix.append(row)
    matrix = np.array(matrix)

    eigenvalues, eigenvectors = eigenvalues_and_eigenvectors(matrix)
    print("The eigenvalues of the matrix are:")
    print(eigenvalues)
    print("The eigenvectors of the matrix are:")
    print(eigenvectors)

if __name__ == "__main__":
    main()
