# Write a program to find the largest of three numbers using if-elif-else.
  a = int(input('Enter the first number:-'))
  b = int(input('Enter the second number:-'))
  c = int(input('Enter the third number:-'))

  if a > b and a > c:
      print('a is the largest number:-',a)
  elif b > a and b > c:
      print('b is the largest number:-',b)
  else:
      print('c is the largest numbber:-',c)
