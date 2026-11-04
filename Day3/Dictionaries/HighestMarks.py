# Write a program to find the student with the highest marks from a dictionary.
  students = {'Jagadeesh':99,'Ravi':89,'Kishore':79,'Major':100}
  highest marks = max(students.values())
  for name,marks in students.items():
      if marks == highest marks:
          print('Student with highest marks is:-',name,'and highest marks is:-',marks)
