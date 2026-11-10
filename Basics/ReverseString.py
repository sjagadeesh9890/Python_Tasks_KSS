# String Reversal: Write a program to reverse a string without using built-in reverse functions.
string = 'Jagadeesh'
reverse_string = ''

for char in string:
    reverse_string = char+reverse_string

print(reverse_string)
