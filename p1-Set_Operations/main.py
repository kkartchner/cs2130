__author__ = "Ky Kartchner"
__date__ = "11 May 2020"

import set_operations as ops

##########################################
# Calculates the union, intersection, and difference of two hard coded
# sets and displays the results using set notation.
##########################################
def main():
    setA = {1, 3, 5, 6, 8}
    setB = {2, 3, 4, 7, 9}
    ops.run_operations(setA, setB)

main()