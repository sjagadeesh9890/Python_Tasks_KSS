# Write a Python program using the random module to generate 10 random integers between 1 and 100 and store them in a list. Print the list.
from random import*
numbers_lis = []
for i in range(10):
    numbers_lis.append(randint(1,100))
print(numbers_lis)
