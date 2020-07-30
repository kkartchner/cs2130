__author__ = "Ky Kartchner"


def get_user_choice(message: str, choices: [str], sentinel_value='q') -> str:
    """Creates a question string and continues to ask it until the user
    provides a valid option
    
    Args: 
        message (str): Decription of the options the user has.
        choices ([str]): Options the user can enter.
        sentinel_value (str): Value the user can enter to exit (default of 'q')
    
    Returns:
        str: The valid option that the user entered 
    """

    user_input = input(
        f"{message} ({'/'.join(e for e in choices)})? ")
    if not (user_input.upper() in choices or user_input.lower() in choices):
        # If user choice is not one of the listed options
        if (user_input == sentinel_value):
            exit_program()
        else:
            print(f"'{user_input}' is not a valid option")
            user_input = get_user_choice(message, choices, sentinel_value)

    return user_input


def exit_program():
    """Prints exit message and then exits the program
    """

    print("\nExiting... Have a nice day!")
    exit()
