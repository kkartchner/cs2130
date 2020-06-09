__author__ = "Ky Kartchner"
__date__ = "6/9/20"

from collections import deque


def main():
    print("\nWelcome to BaseConversions!")
    print("Enter a positive decimal value to see what it is in base 2, base 8, and base 16.")
    print("Type in 'q' to exit at any point.")
    while True:
        raw_input = input("\nInput a decimal: ")
        if raw_input == 'q':
            break
        else:
            try:
                decimal_num = int(raw_input)
            except ValueError:
                print(f"'{raw_input}' is not a decimal number!")
                continue

            try:
                print_conversion(decimal_num, 2)
                print_conversion(decimal_num, 8)
                print_conversion(decimal_num, 16)
            except ValueError as err:
                print(err)


def print_conversion(decimal_num: int, to_base: int):
    try:
        print(f"{decimal_num} in base {to_base}:",
              base_conversion(decimal_num, to_base))
    except ValueError:
        raise


def base_conversion(decimal_num: int, to_base: int) -> str:
    if decimal_num < 0:
        raise ValueError("Invalid input. Only positive numbers are allowed!")

    positional_values = deque()
    x = decimal_num
    while x > 0:
        positional_values.appendleft(x % to_base)
        x //= to_base

    # return the reversed string
    return ''.join(str(num) for num in positional_values)


if __name__ == "__main__":
    main()
