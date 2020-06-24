__author__ = "Ky Kartchner"


def main():
    """Calculates and displays the truth table for the boolean expression
    '(( c + ~d ) * b ) * ~( d + a * e )'.
    """

    print("\nWelcome to Input/Output Table!")
    print("Here is the calculated truth table for boolean expression '(( c + ~d ) * b ) * ~( d + a * e )':\n")

    variables = ['a', 'b', 'c', 'd', 'e']
    expression_header = "(( c + ~d ) * b ) * ~( d + a * e )"

    # print Header:
    print('|'.join(e for e in variables) + '|' + expression_header)
    print('-'*44)

    # print Rows:
    top_row_decimal_value = 2**len(variables) - 1
    # Start from top row (31) and decrease by 1 until hits -1.
    for row_num in range(top_row_decimal_value, -1, -1):
        # Format to n-bit binary number with n being the number of variables. +2 to account for 0b
        # e.g. '#07b' ('0b' followed by 5 bits; 7 characters total):
        format_string = f"#0{len(variables)+2}b"

        # apply format string; truncate '0b'
        # e.g. row_num of 28 becomes '0b11100' then truncated to '11100':
        binary_string = format(row_num, format_string)[2:]

        # Print current row using binary_string separated by '|':
        # spacer_string for centering truth value under expression header
        spacer_string = (' ' * (len(expression_header) // 2))
        print('|'.join(e for e in binary_string) + '|' +
              spacer_string + evaluate_expression(binary_string))

        # Add divider on multiples of 4 to separate into groups of four for easier value checking
        if row_num % 4 == 0:
            print('-'*44)

    print("\nExiting... Have a nice day!")
    exit()


def evaluate_expression(binary_string):
    """Unpack each binary character, convert to int, and store in a variable. Evaluate variables
    using the expression. e.g. '11011' results in a = 1, b = 1, c = 0, d = 1, and e = 1.

    Args: 
        binary_string (str): The binary string of values to use for variables a - e (in order)
    
    Returns:
        str: '1' if expression is true or '0' if expression is false.
    """

    a, b, c, d, e = map(int, list(binary_string))
    # (( c + ~d ) * b ) * ~( d + a * e ):
    expression = ((c or not(d)) and b) and not(d or (a and e))
    return '1' if expression else '0'


if __name__ == "__main__":
    main()
