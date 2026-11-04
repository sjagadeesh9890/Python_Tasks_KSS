# Write a program to check if an element exists in a set.
  s = {1,2,2,3,4,5,55,66,77,99,100}
  search = int(input('Enter a search number:-'))
  if search in s:
      print('Number is exists.')
  else:
      print('Number is not exists.')
