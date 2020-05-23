__author__ = "Ky Kartchner"
__date__ = "5/23/2020"


def main():
    """Prompts the user for a "sentence" to be hashed and then displays the result.
    Continues to prompt user until they enter in sentinel value 'q' to exit.
    """

    print("\nWelcome to SentenceHasher!")
    print("Enter a sentence consisting only of letters and spaces" +
          "(no numbers or other symbols allowed) to receive its hash value.")
    print("If at any point, you are all hashed-out, enter 'q' to exit.")

    while True:
        sentence = input("\nEnter the sentence to be hashed or 'q' to exit: ")
        if sentence == 'q':
            break
        try:
            print("Computed hash is:", hash_sentence(sentence))
        except ValueError as err:
            print(err)


def hash_sentence(sentence: str) -> int:  # ord(a)=97, ord(z)=122
    """Computers the hash of the provided sentence

    Sums the numeric value of each letter in the provided sentence using
    (A=a=1, B=b=2 ... Z=z=26, space=31). 

    Args:
        sentence (str): The sentence to compute the hash value of

    Returns:
        int: The hash value of sentence. f(n) = letter_values_sum mod 31

    Raises:
        ValueError: Invalid input. Only letters and spaces are allowed!
    """

    sum_of_values = 0
    for c in sentence:  # sum the numeric value of each letter in the sentence
        # (use A=a=1, B=b=2 ... Z=z=26, space=31)
        numeric_value = ord(c.lower()) - 96
        if 1 <= numeric_value and numeric_value <= 26:
            sum_of_values += numeric_value
        elif c == ' ':
            sum_of_values += 31
        else:
            raise ValueError(
                "Invalid input. Only letters and spaces are allowed!")

    return sum_of_values % 31  # apply the hash function f(n) = sum mod 31.


main()
