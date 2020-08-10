# cs2130
Programming assignments from my Weber State Computational Structures (CS 2130) class, 
taken Summer 2020 semester.

## Program1 - Set Operations:
Calculates the union, intersection, and difference of two hard coded sets and
displays the results using set notation.

### Output:
```
A = {1, 3, 5, 6, 8}
B = {2, 3, 4, 7, 9}
AuB = {1, 2, 3, 4, 5, 6, 7, 8, 9}
AnB = {3}
A-B = {1, 5, 6, 8}
```
## Program2 - Sentence Hashing:
Prompts the user for a "sentence" to be hashed and then displays the result.
Continues to prompt user until they enter in sentinel value 'q' to exit.

### Example Output:
```
Welcome to SentenceHasher!
Enter a sentence consisting only of letters and spaces(no numbers or other symbols allowed) to receive its hash value.
If at any point, you are all hashed-out, enter 'q' to exit.

Enter the sentence to be hashed or 'q' to exit: hello
Computed hash is: 21

Enter the sentence to be hashed or 'q' to exit:
``` 
## Program3 - Sequence:
Generates and displays the following binary sequence:
11110000111000110010

### Output:
```
11110000111000110010
```
## Program4 - Base Conversions
Prompts the user for a positive decimal value then displays its value in base 2,
base 8, and in base 16. 
Continues to prompt the user until they enter in the sentinel value 'q' to exit.

### Example Output:
```
Welcome to BaseConversions!
Enter a positive decimal value to see what it is in base 2, base 8, and base 16.
Type in 'q' to exit at any point.

Input a decimal: 138
138 in base 2: 10001010
138 in base 8: 212
138 in base 16: 8A

Input a decimal: q

Exiting... Have a nice day!
```
## Program5 - Compound Propositions
Prompts the user for a compound proposition composed of the variables p and q, 
then prints the truth table for the compound proposition

### Example Output:
```
Welcome to Compound Propositions!
Answer three questions to generate a compound proposition and its associated truth table.
If at anytime you decide you have better things to do, enter 'q' to exit.

Do you want to AND or OR the variables (and/or)? and
Do you want to NOT p (y/n)? y
Do you want to NOT q (y/n)? y

Answer:
p  q  ~pA~q
T  T    F
T  F    F
F  T    F
F  F    T

Do you want to AND or OR the variables (and/or)? q  

Exiting... Have a nice day!
```
## Program6 - Input/Output Table 
Calculates and displays the truth table for the boolean expression '(( c + ~d ) * b ) * ~( d + a * e )'.

### Output:
```
Welcome to Input/Output Table!
Here is the calculated truth table for boolean expression '(( c + ~d ) * b ) * ~( d + a * e )':

a|b|c|d|e|(( c + ~d ) * b ) * ~( d + a * e )
--------------------------------------------
1|1|1|1|1|                 0
1|1|1|1|0|                 0
1|1|1|0|1|                 0
1|1|1|0|0|                 1
--------------------------------------------
1|1|0|1|1|                 0
1|1|0|1|0|                 0
1|1|0|0|1|                 0
1|1|0|0|0|                 1
--------------------------------------------
1|0|1|1|1|                 0
1|0|1|1|0|                 0
1|0|1|0|1|                 0
1|0|1|0|0|                 0
--------------------------------------------
1|0|0|1|1|                 0
1|0|0|1|0|                 0
1|0|0|0|1|                 0
1|0|0|0|0|                 0
--------------------------------------------
0|1|1|1|1|                 0
0|1|1|1|0|                 0
0|1|1|0|1|                 1
0|1|1|0|0|                 1
--------------------------------------------
0|1|0|1|1|                 0
0|1|0|1|0|                 0
0|1|0|0|1|                 1
0|1|0|0|0|                 1
--------------------------------------------
0|0|1|1|1|                 0
0|0|1|1|0|                 0
0|0|1|0|1|                 0
0|0|1|0|0|                 0
--------------------------------------------
0|0|0|1|1|                 0
0|0|0|1|0|                 0
0|0|0|0|1|                 0
0|0|0|0|0|                 0
--------------------------------------------

Exiting... Have a nice day!
```
## Program7 - Permutations and Combinations
Prompts the user for n and r values and then computes and displays the
combinations and permutations of the two.

### Example Output:
```
Welcome to Permutations and Combinations!

Enter a postive integer for n and a value for r (that is less than n) to compute 
the permutations and combinations of the two. At any time, enter 'q' to exit.

Enter a value for n: 23
Enter a value for r: 6
Permutation:
 P(23,6)w/repeats: 148,035,889
 P(23,6)w/o repeats: 72,681,840
Combination:
 C(23,6)w/repeats: 376,740
 C(23,6)w/o repeats: 100,947

Enter a value for n: q

Exiting... Have a nice day!
```
## Program8 - Monty Hall
Simulates the Monty Hall 3 doors game and gives the percentage of wins
for when the contestant switches vs. when they don't switch.

### Example Output:
```
Welcome to the Monty Hall 3 Doors Game simulator!

You won 66,954 out of 100,000 times (66.95400%) by switching.
You won 33,112 out of 100,000 times (33.11200%) by NOT switching.

Run another simulation? (y/n)? n

Exiting... Have a nice day!
```
## Program9.1 - Properties of Relations
Prints the calculated properties of several hard-coded matrices.
### Output:
```
Welcome to Properties of Relations!

Below are hard-coded matrices with their calculated properties:

A: 0 1 1 1
   0 0 1 1
   0 0 0 1
   0 0 0 0

anti-reflexive, anti-symmetric, asymmetric
--------------------
B: 0 1 0 0
   0 1 0 0
   0 0 0 1
   1 0 0 0

anti-symmetric
--------------------
C: 0 1 0 1
   1 0 1 0
   0 1 0 1
   1 0 1 0

anti-reflexive, symmetric
--------------------
D: 1 1 0 1
   1 1 1 0
   0 1 1 1
   1 0 1 1

reflexive, symmetric
--------------------
E: 1 1 1 1
   1 1 1 1
   1 1 1 1
   1 1 1 1

reflexive, symmetric
--------------------
F: 0 0 0 0
   0 0 0 0
   0 0 0 0
   0 0 0 0

anti-reflexive, symmetric, anti-symmetric, asymmetric
--------------------

Exiting... Have a nice day!
```
## Program9.2 - Matrix Operations
Prompt the user to select two of the four hard-coded matrices and
to select whether to multiply or add the matrices together.

### Example Output:
```
Welcome to Matrix Operations!

Select two of the matrices below, then select if you want to add or multiply them.
Enter 'q' at any time to exit.

A: 4 -1
   2 8

B: 2 3 9
   -3 3 7

C: 1 -4
   9 3
   -8 2

D: 3 8 3
   -2 7 1
   0 -1 8

Select the first matrix (A/B/C/D)? a
Select the second matrix (A/B/C/D)? b
Would you like to add, or multiply them? (A/M)? m
A: 4 -1
   2 8

B: 2 3 9
   -3 3 7

A x B: 11 9 29
       -20 30 74

Select the first matrix (A/B/C/D)? d
Select the second matrix (A/B/C/D)? d
Would you like to add, or multiply them? (A/M)? a
D: 3 8 3
   -2 7 1
   0 -1 8

D: 3 8 3
   -2 7 1
   0 -1 8

D + D: 6 16 6
       -4 14 2
       0 -2 16

Select the first matrix (A/B/C/D)? a
Select the second matrix (A/B/C/D)? d
Would you like to add, or multiply them? (A/M)? m
A: 4 -1
   2 8

D: 3 8 3
   -2 7 1
   0 -1 8

Invalid. You cannot multiply  A and D together

Select the first matrix (A/B/C/D)? q

Exiting... Have a nice day!
```
## Program10 - Tree Traversal
Create a binary tree with hard-coded input and then print its 
pre-order, in-order, and post-order traversals.

### Output:
```
Welcome to Tree Traversal!
Below is the input order of a hard-coded tree and its calculated traversals:
BST input order: 50, 75, 25, 15, 60, 35, 90, 42, 20, 27, 5, 55, 95, 80, 70

pre-order: 50, 25, 15, 5, 20, 35, 27, 42, 75, 60, 55, 70, 90, 80, 95
in-order: 5, 15, 20, 25, 27, 35, 42, 50, 55, 60, 70, 75, 80, 90, 95
post-order: 5, 20, 15, 27, 42, 35, 25, 55, 70, 60, 80, 95, 90, 75, 50
```
