__author__ = "Ky Kartchner"


def main():
    """Prompts the user for a compound proposition composed of the variables
    p and q, then prints the truth table for the compound proposition
    """

    print("\nWelcome to Compound Propositions!")
    print("Answer three questions to generate a compound proposition and its" +
          " associated truth table.")
    print("If at anytime you decide you have better things to do, enter 'q' to exit.")

    while True:
        print()
        operation = get_choice("AND or OR the variables", "and", "or")
        not_p = get_choice("NOT p", "y", "n")
        not_q = get_choice("NOT q", "y", "n")

        compound_proposition = compound(operation, not_p, not_q)

        predicate = generate_compound_predicate(compound_proposition)

        print("\nAnswer:")
        print(f"p  q  {compound_proposition}")
        print(f"T  T  {predicate(True, True)}")
        print(f"T  F  {predicate(True, False)}")
        print(f"F  T  {predicate(False, True)}")
        print(f"F  F  {predicate(False, False)}")


def compound(operation: str, not_p: str, not_q: str) -> str:
    return (("p" if not_p == 'n' else "~p") + ("A" if operation == "and" else "V")
            + ("q" if not_q == 'n' else "~q"))


def generate_compound_predicate(compound_proposition: str):
    """Generates and returns a lamda function from the provided compound proposition

    Args:
        compound_proposition (str): The proposition string to create the function from (e.g. "pVq")

    Returns:
        lamda (p, q): A lamda function with input p and q that evaluates to what the compound 
            proposition would evaluate to given the same p and q.
    """

    function_string = compound_proposition.replace(
        "A", " and ").replace("V", " or ")
    function_string = not_the_tilded_variables(function_string)

    return lambda p, q: "T" if eval(function_string) else "F"


def not_the_tilded_variables(function_string):
    return function_string


def get_choice(options: str, choice1: str, choice2: str, sentinel_value='q') -> str:
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
        if (user_input == sentinel_value):
            exit_program()
        else:
            print(f"'{user_input}' is not a valid option")
            user_input = get_choice(options, choice1, choice2)

    return user_input


def exit_program():
    """Prints exit message and then exits the program
    """

    print("\nExiting... Have a nice day!")
    exit()


if __name__ == "__main__":
    main()
