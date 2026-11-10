#Write a program that uses random.choice() to randomly select a student from a list and display: 
"The selected student for presentation is: <name>."
from random import*
students = ['jagadeesh','Rahul','Vamsi','Rajesh']
selected_student = choice(students)
print('The selected student for presentation is:',selected_student)
