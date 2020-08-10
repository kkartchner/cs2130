__author__ = "Ky Kartchner"

from functools import reduce
from operator import add
from matrices import matrices


def main() -> None:
    """Prints the calculated properties of several hard-coded matrices.
    """

    print("\nWelcome to Properties of Relations!\n")
    print("Below are hard-coded matrices with their calculated properties:\n")

    for i, matrix in enumerate(matrices):
        print_matrix(matrix, chr(ord('A')+i))

    exit_program()


def matrix_properties(array: [[int]]) -> str:
    reflexiveness = get_reflexiveness(array)
    properties = [reflexiveness, *get_symmetry(array, reflexiveness)]
    property_string = ', '.join(e for e in properties if e != "")
    return property_string if property_string != "" else "none"


def get_reflexiveness(array: [[int]]) -> str:
    diagonal_values = list(map(lambda x: array[x][x], range(len(array))))
    diagonal_sum = reduce(add, diagonal_values)
    if diagonal_sum == len(array):  # All are one
        return "reflexive"
    elif diagonal_sum == 0:  # All are zero
        return "anti-reflexive"
    else:  # Not all the same
        return ""


def get_symmetry(array: [[int]], reflexiveness: str) -> [str]:
    corresponding_sums = []
    # Loop over each element below the diagonal and add its value to its
    # corresponding element above the diagonal(e.g. (2, 1) + (1, 2) = 1 + 1 = 2)
    # sum of 2 = two-way path, sum of 1 = one-way path, sum of 0 = no path:
    for row in range(1, len(array)):
        for col in range(row):
            corresponding_sums.append(array[row][col] + array[col][row])

    # Count the number of 2's, 1's, and 0's contained in corresponding_sums:
    sum_counts = [0, 0, 0]
    for s in corresponding_sums:
        sum_counts[s] += 1

    symmetries = []
    # symmetric if only contains 2's and 0's (only two way paths):
    if sum_counts[1] == 0:
        symmetries.append("symmetric")

    # anti-symmetric if only contains 1's and 0's (only one-way paths,
    # but can have self-loops):
    if sum_counts[2] == 0:
        symmetries.append("anti-symmetric")
        if (reflexiveness == "anti-reflexive"):
            # asymmetric if no self-loops (i.e. anti-reflexive))
            symmetries.append("asymmetric")

    return symmetries


def print_matrix(array: [[int]], label: str) -> None:
    print(f"{label}: ", end="")
    print(' '.join(str(e) for e in array[0]))
    for row in array[1:]:
        print("  ", ' '.join(str(e) for e in row))

    print(f'\n{matrix_properties(array)}')
    print('-'*20)


def exit_program():
    """Prints exit message and then exits the program
    """

    print("\nExiting... Have a nice day!")
    exit()


if __name__ == "__main__":
    main()
