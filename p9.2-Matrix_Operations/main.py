__author__ = "Ky Kartchner"

from helpers import get_user_choice
from matrices import matrices


def main() -> None:
    """Prompt the user to select two of the four hard-coded matrices and
    to select whether to multiply or add the matrices together.
    """

    print("\nWelcome to Matrix Operations!\n")
    print("Select two of the matrices below, then select if you want to"
          + " add or multiply them.")
    print("Enter 'q' at any time to exit.\n")

    matrix_dictionary = {}
    # Initialize matrix dictionary by assigning a letter to
    #   each matrix in matrices:
    for i, matrix in enumerate(matrices):
        key = chr(ord('A')+i)
        matrix_dictionary[key] = matrix
        print_matrix(matrix, key)

    while True:
        first_matrix_key = get_user_choice(
            "Select the first matrix", matrix_dictionary.keys()).upper()
        second_matrix_key = get_user_choice(
            "Select the second matrix", matrix_dictionary.keys()).upper()

        operation = get_user_choice("Would you like to add, or multiply them?",
                                    ['A', 'M']).upper()

        first_matrix = matrix_dictionary[first_matrix_key]
        second_matrix = matrix_dictionary[second_matrix_key]

        print_matrix(first_matrix, first_matrix_key)
        print_matrix(second_matrix, second_matrix_key)

        if operation_valid(first_matrix, second_matrix, operation):
            op_func = add_matrices if operation == 'A' else multiply_matrices
            op_symbol = '+' if operation == 'A' else 'x'

            print_matrix(op_func(first_matrix, second_matrix),
                         f"{first_matrix_key} {op_symbol} {second_matrix_key}")
        else:
            full_operation = 'add' if operation == 'A' else 'multiply'

            print(f"Invalid. You cannot {full_operation} ",
                  f"{first_matrix_key} and {second_matrix_key} together\n")


def print_matrix(matrix: [[int]], label: str) -> None:
    """Print the provided matrix into a format such as the following: 
    A: 1 4 2
       2 3 -1
    
    Args:
        matrix ([[int]]): The matrix to print
        label: The label to print for the matrix
    """

    label += ": "
    print(label, end="")
    print(' '.join(str(e) for e in matrix[0]))
    for row in matrix[1:]:
        print(" " * (len(label)-1), ' '.join(str(e) for e in row))
    print()


def operation_valid(first_matrix: [[int]], second_matrix: [[int]],
                    operation: str) -> bool:
    """Checks if performing the provided operation on the provided
    matrices is valid.

    Args:
        first_matrix ([[int]]): The first matrix
        second_matrix ([[int]]): The second matrix
        operation (str): The operation to check against ('A' or 'M')
    
    Returns:
        bool: True if operation is valid; False if it is not.
    """

    m1 = len(first_matrix)  # first_matrix is m1 x n1
    n1 = len(first_matrix[0])

    m2 = len(second_matrix)  # second_matrix is m2 x n2
    n2 = len(second_matrix[0])

    if operation == 'A':
        return m1 == m2 and n1 == n2  # matrices are same size
    elif operation == 'M':
        return n1 == m2  # middle numbers the same

    return False


def add_matrices(first_matrix: [[int]], second_matrix: [[int]]) -> [[int]]:
    """Add the provided matrices together

    Args:
        first_matrix ([[int]]): The first matrix
        second_matrix ([[int]]): The second matrix
    
    Returns:
        [[int]]: The result of adding first_matrix and second_matrix together
    """

    result_matrix = []
    for y in range(len(first_matrix)):
        row = []
        for x in range(len(first_matrix[y])):
            row.append(first_matrix[y][x] + second_matrix[y][x])
        result_matrix.append(row)

    return result_matrix


def multiply_matrices(first_matrix: [[int]], second_matrix: [[int]]) -> [[int]]:
    """Multiply the first provided matrix by the second provided matrix.
    Multiply each row of the first matrix by each column of the second matrix

    Args:
        first_matrix ([[int]]): The first matrix
        second_matrix ([[int]]): The second matrix

    Returns:
        [[int]]: The result of multiplying first_matrix by second_matrix
    """

    result_matrix = []  # m1 X n2: len(first_matrix) X len(second_matrix[0])
    for y in range(len(first_matrix)):
        row = []
        for x in range(len(second_matrix[0])):
            entry = 0
            for k in range(len(first_matrix[0])):
                entry += (first_matrix[y][k] * second_matrix[k][x])
            row.append(entry)
        result_matrix.append(row)

    return result_matrix


if __name__ == "__main__":
    main()
