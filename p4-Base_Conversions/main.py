__author__ = "Ky Kartchner"
__date__ = "6/12/20"

from collections import deque


def main():
    """Prompts the user for a positive decimal value then displays its value in base 2,
    base 8, and in base 16. Continues to prompt the user until they enter in the sentinel
    value 'q' to exit.
    """

    print("\nWelcome to BaseConversions!")
    print("Enter a positive decimal value to see what it is in base 2, base 8, and base 16.")
    print("Type in 'q' to exit at any point.")
    while True:
        raw_input = input("\nInput a decimal: ")
        if raw_input.lower() == 'q':
            break
        else:
            try:
                # Throws ValueError if not an integer
                decimal_num = int(raw_input)
                print_conversion(decimal_num, 2)
                print_conversion(decimal_num, 8)
                print_conversion(decimal_num, 16)
            except ValueError:
                print(
                    f"Invalid input '{raw_input}'. Only positive integers are allowed!")

    print("\nExiting... Have a nice day!")


def print_conversion(decimal_num: int, to_base: int):
    """Prints the result of the specified base_conversion
    
    Args:
        decimal_num (int): The decimal number to convert
        to_base (int): The base to convert to
    """

    print(f"{decimal_num} in base {to_base}:",
          base_conversion(decimal_num, to_base))


def base_conversion(decimal_num: int, to_base: int) -> str:
    """Converts the specified decimal number to the specified base

    Args: 
        decimal_num (int): The decimal number to convert
        to_base (int): The base to convert to

    Returns:
        str: The value of the number in the new base

    Raises:
        ValueError: Only positive integers allowed!
    """

    if decimal_num < 0:  # Raise error if decimal_num is negative
        raise ValueError("Only positive integers allowed!")
    elif decimal_num == 0:
        return "0"

    x = decimal_num
    # Using double ended queue for O(1) adding of values to beginning of list.
    positional_values = deque()
    while x > 0:
        value = x % to_base
        if value > 9:
            # Get the character that is (value % 10) away from "A"
            value = chr(ord("A") + (value % 10))

        # Add value to beginning (left-most) of the deque
        positional_values.appendleft(value)
        x //= to_base

    # Combine the elements into a string
    return ''.join(str(num) for num in positional_values)


if __name__ == "__main__":
    # Only run if being ran as main program
    main()
