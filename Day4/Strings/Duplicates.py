#  Write a program to remove duplicate characters from a string.
   string = 'jagadeesh'
   result = ''
   for char in string:
       if char not in result:
           result += char
   print(result)
