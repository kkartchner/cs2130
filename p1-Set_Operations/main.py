##########################################
# Author: Ky Kartchner
# Date: 10 May 2020

##########################################
# Calculates the union, intersection, and difference of two hard coded
# sets and displays the results using set notation.
##########################################
def main():
    setA = {1, 3, 5, 6, 8}
    setB = {2, 3, 4, 7, 9}
    run_operations(setA, setB)

##########################################
# Return the union of set1 and set2
##########################################
def union(set1, set2):
    result = set(set1) # copy set1 into result 
    result.update(set2) # add set2 elements to result set
    return result

##########################################
# Return the intersection of set1 and set2
##########################################
def intersect(set1, set2):
    shorter_set = None
    longer_set = None
    result = set()

    # determine which set is longer and which is shorter to help increase performance:
    if (len(set1) < len(set2)):
        shorter_set = set1
        longer_set = set2
    else:
        shorter_set = set2
        longer_set = set1

    # compare each element of the shorter set to see if it also exists in the longer set:
    for v in shorter_set: 
        if v in longer_set: 
            result.add(v)

    return result

##########################################
# Return set1 - set2
##########################################
def difference(set1, set2):
    result = set(set1) # create new set and copy set1 values into it
    for e in set2: # for each element in set2
        if (e in set1): # remove from set1
            result.remove(e)

    return result

##########################################
# Print the specified set in sorted set notation 
##########################################
def print_set(set_name, set_values):
    sorted_values = sorted(set_values, key=int)
    print(set_name, "= {" + ', '.join(str(e) for e in sorted_values) + "}")

##########################################
# Run the various set functions and print the results
##########################################
def run_operations(set1, set2):
    print_set('A', set1)
    print_set('B', set2)
    print_set('AuB', union(set1, set2))
    print_set('AnB', intersect(set1, set2))
    print_set('A-B', difference(set1, set2))
    print()

main()
