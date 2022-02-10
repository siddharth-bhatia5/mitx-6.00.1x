"""
MITx 6.00.1x - Problem Set #1
"""

"""
Problem #1: 10/10

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', 
your program should print:

`Number of Vowels: 5`
"""
def num_of_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u'] # vowels list
    count = 0

    for char in s: # loops through each character
        if char in vowels: # checks whether character exists in list
            count += 1
    return "Number of Vowels: " + str(count)
print(num_of_vowels('azcbobobegghakl'))

"""
Problem #2: 10/10

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 

For example, if s = 'azcbobobegghakl', then your program should print:

`Number of times bob occurs is: 2`
"""
def num_of_bob(s):
    count = 0
    for i in range(0, len(s)): # prevents IndexOutOfBoundsError
        substring = s[i:i+3] # looks whether three character substring equals bob
        if substring == 'bob':
            count += 1
    return("Number of times bob occurs is: " + str(count))
print(num_of_bob('azcbobobegghakl'))

"""
Problem #3: 15/15

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 

For example, if s = 'azcbobobegghakl', then your program should print:

`Longest substring in alphabetical order is: beggh`

In the case of ties, print the first substring. 

For example, if s = 'abcbcd', then your program should print:

`Longest substring in alphabetical order is: abc`

Note: This problem may be challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, 
we suggest that you move on to a different part of the course. 
If you have time, come back to this problem after you've had a break and cleared your head.
"""
def longest_substring(s):
    current = ''
    longest = ''
    for i in range(len(s)):
        if (s[i] >= s[i-1]): # checks whether following letter is greater than previous alphabetically
            current += s[i]
        else:
            current = s[i]
        if len(current) > len(longest): # updates longest substring
            longest = current
    return("Longest substring in alphabetical order is: " + longest)
print(longest_substring('azcbobobegghakl'))
print(longest_substring('abcbcd'))