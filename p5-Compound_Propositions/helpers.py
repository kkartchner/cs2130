def get_user_choice(options: str, choice1: str, choice2: str, sentinel_value='q') -> str:
    """Creates a question string and continues to ask it until the user
    provides a valid option
    
    Args: 
        options (str): Decription of the options the user has (e.g. "AND or OR the variables")
        choice1 (str): The user's first option they can enter (e.g. "and")
        choice2 (str): The user's second option they can enter (e.g. "or")
        sentinel_value (str): Value the user can enter to exit (default of 'q')
    
    Returns:
        str: The valid option that the user entered 
    """

    user_input = input(f"Do you want to {options} ({choice1}/{choice2})? ")
    if not (user_input == choice1 or user_input == choice2):
        # If user choice is not one of the listed options
        if (user_input == sentinel_value):
            exit_program()
        else:
            print(f"'{user_input}' is not a valid option")
            user_input = get_user_choice(options, choice1, choice2)

    return user_input


def exit_program():
    """Prints exit message and then exits the program
    """

    print("\nExiting... Have a nice day!")
    exit()


def compound(operation: str, not_p: str, not_q: str) -> str:
    """Generates and returns a function string 

    Args:
        operation (str): The operation to use. "and" or "or" are the two possible operations.
        not_p (str): Whether or not p should be negated
        not_q (str): Whether or not q should be negated

    Returns:
        str: The generated function string
    """

    return (("p" if not_p == 'n' else "not(p)") + f" {operation} "
            + ("q" if not_q == 'n' else "not(q)"))


def generate_predicate(function_string: str):
    """Generates and returns a lamda function from the provided function string

    Args:
        function_string (str): The function string to create the predicate from 

    Returns:
        lamda (p, q): A lamda function with input p and q that evaluates to what the
            function string would evaluate to given the same p and q.
    """

    return lambda p, q: "T" if eval(function_string) else "F"


def string_to_proposition(function_string) -> str:
    """Converts the provided function string to a compound proposition by
    replacing not(x) with ~x, " and " with 'A', and " or " with 'V'. 

    Args:
        function_string (str): The function string to convert
    Returns:
        str: The converted compound proposition
    """

    return function_string.replace("not(", "~").replace(")", "").replace(" and ", "A").replace(" or ", "V")
