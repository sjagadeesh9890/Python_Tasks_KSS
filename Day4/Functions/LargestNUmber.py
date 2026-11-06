# Write a Python program with a function that returns the largest of three numbers.
def largest_number(a,b,c):

      if a >= b and a >= c:
          return a
      elif b >= a and b >= c:
          return b
      else:
          return c

a = int(input('Enter a number:-'))
b = int(input('Enter a number:-'))
c = int(input('Enter a number:-'))
print('largest number is:-',largest_number(a,b,c))
