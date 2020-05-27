__author__ = "Ky Kartchner"
__date__ = "5/26/20"


def main():
    """Generate and display the following binary sequence:
    11110000111000110010
    """

    sequence = ''
    for i in range(4, 0, -1):  # loop from 4 down to 0, decrementing by one each time
        # Add i 1's and i 0's to the sequence string
        sequence += ('1'*i + '0'*i)

    print(sequence)


main()
