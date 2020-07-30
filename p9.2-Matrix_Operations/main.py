__author__ = "Ky Kartchner"

from helpers import get_user_choice
from matrices import matrices


def main():
    print("\nWelcome to Matrix Operations!\n")
    print("Select two of the matrices below, then select if you want to"
          + " add or multiply them.")
    print("Enter 'q' at any time to exit.\n")

    matrix_dictionary = {}
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

        if operation_valid(matrix_dictionary[first_matrix_key],
                           matrix_dictionary[second_matrix_key], operation):
            # perform operation
            if operation == 'A':
                print_matrix(add_matrices(matrix_dictionary[first_matrix_key],
                                          matrix_dictionary[second_matrix_key]),
                             f"{first_matrix_key} + {second_matrix_key}")
            elif operation == 'M':
                print_matrix(multiply_matrices(matrix_dictionary[first_matrix_key],
                                               matrix_dictionary[second_matrix_key]),
                             f"{first_matrix_key} x {second_matrix_key}")
                pass
        else:
            full_operation = 'add' if operation == 'A' else 'multiply'
            print(f"Invalid. You cannot {full_operation} ",
                  f"{first_matrix_key} and {second_matrix_key} together")

            print()


def print_matrix(array: [[int]], label: str) -> None:
    label += ": "
    print(label, end="")
    print(' '.join(str(e) for e in array[0]))
    for row in array[1:]:
        print(" " * (len(label)-1), ' '.join(str(e) for e in row))
    print()


def operation_valid(first_matrix, second_matrix, operation):
    first_rows = len(first_matrix)
    first_cols = len(first_matrix[0])

    second_rows = len(second_matrix)
    second_cols = len(second_matrix[0])

    if operation == 'A':
        return first_rows == second_rows and first_cols == second_cols
    elif operation == 'M':
        return first_cols == second_rows


def add_matrices(first_matrix, second_matrix):
    result_matrix = []
    for y in range(len(first_matrix)):
        row = []
        for x in range(len(first_matrix[y])):
            row.append(first_matrix[y][x] + second_matrix[y][x])
        result_matrix.append(row)

    return result_matrix


def multiply_matrices(first_matrix, second_matrix):
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
