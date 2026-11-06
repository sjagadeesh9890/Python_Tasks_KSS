#  Write a function that returns the factorial of a number.
   def factorial(num):
       fact = 1
       for i in range(1, num+1):
           fact *= 1
       return fact

    n = int(input('Enter a number:-'))
    print(factorial(n))
