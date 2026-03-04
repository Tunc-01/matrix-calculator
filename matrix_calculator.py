import numpy as np

def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))

    matrix = []

    print(f"Enter values row by row for {name}")

    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)

    return np.array(matrix)


def matrix_addition(A, B):
    return A + B


def matrix_subtraction(A, B):
    return A - B


def matrix_multiplication(A, B):
    return np.dot(A, B)


def matrix_transpose(A):
    return np.transpose(A)


def matrix_determinant(A):
    return np.linalg.det(A)


def matrix_inverse(A):
    return np.linalg.inv(A)


def matrix_eigenvalues(A):
    values, vectors = np.linalg.eig(A)
    return values, vectors


def print_matrix(M, name="Result"):
    print(f"\n{name}:")
    print(M)


def menu():

    print("\nMatrix Calculator")
    print("1 - Matrix Addition")
    print("2 - Matrix Subtraction")
    print("3 - Matrix Multiplication")
    print("4 - Matrix Transpose")
    print("5 - Determinant")
    print("6 - Matrix Inverse")
    print("7 - Eigenvalues")
    print("8 - Exit")


def main():

    while True:

        menu()

        choice = input("Select operation: ")

        if choice == "1":

            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")

            result = matrix_addition(A, B)

            print_matrix(result)

        elif choice == "2":

            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")

            result = matrix_subtraction(A, B)

            print_matrix(result)

        elif choice == "3":

            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")

            result = matrix_multiplication(A, B)

            print_matrix(result)

        elif choice == "4":

            A = input_matrix("Matrix A")

            result = matrix_transpose(A)

            print_matrix(result)

        elif choice == "5":

            A = input_matrix("Matrix")

            result = matrix_determinant(A)

            print("\nDeterminant:", result)

        elif choice == "6":

            A = input_matrix("Matrix")

            result = matrix_inverse(A)

            print_matrix(result, "Inverse Matrix")

        elif choice == "7":

            A = input_matrix("Matrix")

            values, vectors = matrix_eigenvalues(A)

            print("\nEigenvalues:")
            print(values)

            print("\nEigenvectors:")
            print(vectors)

        elif choice == "8":

            print("Exiting program.")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
