# Write a program that searches for a number in a list and breaks the loop when found.
  numbers = [11,22,33,44,55,66,77,88,99]
  search = int(input('Enter a number:-'))
  for i in numbers:
      if i == 77:
          print('Number found',i)
          break
  else:
      print('Number not found')
