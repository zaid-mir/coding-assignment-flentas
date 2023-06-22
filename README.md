# coding-assignment-flentas
Coding Assignment for Flentas

# Permutation in Text Checker

This repository contains a Python program that checks if any permutation of a given pattern exists in a text string. The program uses the sliding window technique for efficient searching.

## Problem Statement

Sherlock Holmes is working on a case. One day going through evidence, he finds some scribbled text at corner of victim's diary. Now Sherlock believes that the scribbled text has something to do with the clue leading to Murderer, so he decides to find every occurrence of all the permutations of the scribbled text in the entire book. Since this is a huge task, he needs your help, he needs you to figure out if any permutation of the scribbled text exists in the given text string, so he can save time with the case. Permutation means any sequence of the string.

## Implementation Details

The program is implemented in Python and follows the sliding window technique to efficiently find permutations of the pattern in the text string. It utilizes the `Counter` class from the `collections` module to count the occurrences of characters in the pattern and the current window of the text.

The algorithm performs the following steps for each test case:

1. The code starts by importing the Counter class from the collections module. 

2. The check_permutation function takes two parameters: pattern and text. This function checks if any permutation of the pattern exists in the text string. It uses the sliding window technique to efficiently compare the character frequencies between the pattern and the current window of the text.

3. The code prompts the user to enter the number of test cases using the input() function and converts the input to an integer using int().

4. A loop is used to iterate over each test case. The loop runs T times, where T is the number of test cases.

5. Inside the loop, the code prompts the user to enter the pattern using input() and stores it in the pattern variable.

6. The code then prompts the user to enter the text string using input() and stores it in the text variable.

7. The check_permutation function is called with the pattern and text variables as arguments, and the result is stored in the result variable.

8. Finally, the result is printed using the print() function. The program handles multiple test cases efficiently and provides a clear "YES" or "NO" result for each test case.



