# Dictionary Operations: Create a dictionary containing student names and marks. Add a new student, update an existing student's marks, and print all student details.
students = {'jagadeesh':99,'raju':89,'kishore':78}
students['Amir'] = 100
students['raju'] = 200
for name,marks in students.items():
    print(name,':-',marks)
