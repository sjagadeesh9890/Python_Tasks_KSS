#  Write a Python program that generates 20 random numbers between 1 and 200 using the random module and store them in a list. 
'''Then using the math module, compute and display: 
● Maximum value 
● Minimum value 
● Square root of the maximum number 
● Logarithm of the minimum number'''
from random import*
from math import*
numbers = []
for i in range(20):
    numbers.append(randint(1,200))
print('Random numbers:-',numbers)
max_value = max(numbers)
min_value = min(numbers)
print('maximum value is:-',max_value)
print('Minimum value is:-',min_value)
print('Square root of the maximum number:-',sqrt(max_value))
print('Logarithm of the minimum number is:-',log(min_value))
