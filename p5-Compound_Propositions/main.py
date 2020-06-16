__author__ = "Ky Kartchner"

import helpers as h


def main():
    """Prompts the user for a compound proposition composed of the variables
    p and q, then prints the truth table for the compound proposition
    """

    print("\nWelcome to Compound Propositions!")
    print("Answer three questions to generate a compound proposition and its" +
          " associated truth table.")
    print("If at anytime you decide you have better things to do, enter 'q' to exit.\n")

    while True:
        operation = h.get_user_choice("AND or OR the variables", "and", "or")
        not_p = h.get_user_choice("NOT p", "y", "n")
        not_q = h.get_user_choice("NOT q", "y", "n")

        function_string = h.compound(operation, not_p, not_q)

        predicate = h.generate_predicate(function_string)

        print("\nAnswer:")
        print(f"p  q  {h.string_to_proposition(function_string)}")
        print(f"T  T    {predicate(True, True)}")
        print(f"T  F    {predicate(True, False)}")
        print(f"F  T    {predicate(False, True)}")
        print(f"F  F    {predicate(False, False)}\n")


if __name__ == "__main__":
    main()
