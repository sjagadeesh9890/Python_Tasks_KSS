# Write a program to assign grades based on marks (for example: A, B, C, Fail). 
  marks = int(input('Enter your marks:-'))

  if marks < 0 and marks >100:
      print('Invalid marks you entered!.')
  elif marks >=90:
      print('You secure A grade.')
  elif marks >= 79:
      print('You secure B grade.')
  elif marks >= 45:
      print('You secure C grade.')
  else:
      print('You are fail.')
