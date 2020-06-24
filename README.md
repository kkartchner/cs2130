# cs2130
Programming assignments from my Weber State Computational Structures (CS 2130) class, taken Summer 2020 semester.

## Program1 - Set Operations:
Calculates the union, intersection, and difference of two hard coded sets and displays the results using set notation.

### Output:
```
A = {1, 3, 5, 6, 8}
B = {2, 3, 4, 7, 9}
AuB = {1, 2, 3, 4, 5, 6, 7, 8, 9}
AnB = {3}
A-B = {1, 5, 6, 8}
```
## Program2 - Sentence Hashing:
Prompts the user for a "sentence" to be hashed and then displays the result. Continues to prompt user until they enter in sentinel value 'q' to exit.

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
Prompts the user for a positive decimal value then displays its value in base 2, base 8, and in base 16. 
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
Prompts the user for a compound proposition composed of the variables p and q, then prints the truth table for the compound proposition
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