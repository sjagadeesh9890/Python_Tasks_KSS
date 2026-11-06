# Write a function to check whether a number is even or odd.
  def even_odd(number):
      if number %2 == 0:
          return 'Even'
      else:
          return 'Odd'

   n = int(input('Enter a number:-'))
   print(even_odd(n))
