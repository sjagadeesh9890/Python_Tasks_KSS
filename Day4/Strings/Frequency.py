# Write a program to count the frequency of each character in a string.
  string = 'jagadeesh'
  for char in string:
      count = 0
      for char1 in string:
          if char == char1:
              count += 1
      print(char,':-',count)
