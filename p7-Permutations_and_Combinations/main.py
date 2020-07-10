__author__ = "Ky Kartchner"

from math import factorial
from functools import reduce


def main() -> None:
    """Prompts the user for n and r values and then computes and displays the
    combinations and permutations of the two.
    """

    print("\nWelcome to Permutations and Combinations!")
    print("\nEnter a postive integer for n and a value for r (that is less"
          + " than n) to compute the permutations and combinations of the two."
          + " At any time, enter 'q' to exit.")

    while True:
        n = get_positive_integer("\nEnter a value for n: ")
        r = get_positive_integer("Enter a value for r: ")
        if n < r:
            print(f"n ({n}) is less than r ({r}). Calculation not possible.")
            continue

        print("Permutation:")
        print_answer(False, n, r, True)
        print_answer(False, n, r, False)

        print("Combination:")
        print_answer(True, n, r, True)
        print_answer(True, n, r, False)


def get_positive_integer(message: str, sentinel_value='q') -> int:
    """Prompts the user with a message until they provide a positive 
    integer value or exits if sentinel value is entered.

    Args:
        message (str): The message to prompt the user with.
        sentinel_value (str): The character that user can enter to exit program
            (default value of 'q')
    
    Returns:
        int: The positive integer value entered by the user.

    Raises:
        ValueError: If user input is not a positive integer
    """

    user_input = input(message)
    if user_input == sentinel_value:
        exit_program()
    else:
        try:
            # Raises ValueError if user_input is not an integer
            user_input = int(user_input)
            if user_input < 0:
                raise ValueError
        except ValueError:
            print(f"Invalid input! '{user_input}' is not a positive integer")
            user_input = get_positive_integer(message)

    return user_input


def permutation(n: int, r: int, repeats: bool) -> int:
    """Calculates and returns the permutation of n and r.
    
    Args:
        n (int): The positive integer value to use for n
        r (int): The positive integer value to use for r
        repeats(bool): Calculated allowing repeats if true; no repeats if false.
    Returns:
        int: The answer to the permutation of n and r
    """

    if repeats:
        return n**r
    else:
        # n!/(n-r)! is the same as performing n * (n-1) *...* (n-r)
        return reduce((lambda x, y: x * y), list(range(n, n-r, -1)))


def combination(n: int, r: int, repeats: bool) -> int:
    """Calculates and returns the combination of n and r.
    
    Args:
        n (int): The positive integer value to use for n
        r (int): The positive integer value to use for r
        repeats(bool): Calculated allowing repeats if true; no repeats if false.
    Returns:
        int: The answer to the combination of n and r
    """

    if repeats:
        return combination((n + r - 1), r, False)
    else:
        # The larger of the two denominator factorials will always factor
        # out of the n! numerator. For example:
        # C(7, 4) = 7! / (4!*3!)
        # = (7 * 6 * 5 * 4!) / (4! * 3!)
        # = (7 * 6 * 5) / 3!
        factorial_stop = max(r, (n - r))
        simplified_numerator = reduce(
            (lambda x, y: x * y), list(range(n, factorial_stop, -1)))
        return (simplified_numerator // factorial(min(r, (n - r))))


def print_answer(is_combination: bool, n: int, r: int, repeats: bool) -> None:
    """Print the answer to either the combination or permutation of n and r.

    Args:
        is_combination (bool): Answer is combination of n and r if true; 
            permutation if false.
        n (int): The positive integer value to use for n
        r (int): The positive integer value to use for r
        repeats(bool): Calculated allowing repeats if true; no repeats if false.
    """

    repeat_string = "w/repeats" if repeats else "w/o repeats"
    type_character = "C" if is_combination else "P"
    answer = combination(
        n, r, repeats) if is_combination else permutation(n, r, repeats)

    print(f" {type_character}({n},{r}){repeat_string}: {'{:,}'.format(answer)}")


def exit_program() -> None:
    """Prints exit message and then exits the program
    """

    print("\nExiting... Have a nice day!")
    exit()


if __name__ == "__main__":
    main()
