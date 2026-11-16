''' Develop a Python program to manage student marks for three subjects. Store the subject 
names in a tuple, maintain unique student names in a set, and store each student’s marks 
in a list inside a dictionary where the key is the student name. Create user-defined 
functions to add a student with marks, display all student records, and calculate the average 
marks of a student. Implement a recursive function to calculate the total marks from the list of 
marks. The program should interact with the user through a simple menu. Also include 
exception handling to handle ValueError (non-numeric marks input), ZeroDivisionError 
(average calculation issues), TypeError (incorrect data type in marks), and NameError (when a 
student name entered does not exist in the dictionary).'''

subjects = ('Math','Science','English')
students = set()
student_marks = {}

def add_students():
    name = input('Enter a student name:-')
    print('Student name:-',name)

    if name in students:
        print('Student already exists')
        return
    
    marks =[]

    for subject in subjects:
        try:
            mark = int(input('Enter marks for ' + subject + ':-'))
            marks.append(mark)

        except ValueError:
            print('Invalid input! Please enter numeric marks')
            return
    
    students.add(name)
    student_marks[name] = marks

    print('Student added sucessfully')
    print(student_marks)

def display_students():
    if not student_marks:
        print('No student records found')
        return
    
    for name,marks in student_marks.items():
        print(name,':-',marks)

def recursive_total(marks):
    if len(marks) == 0:
        return 0
    return marks[0] + recursive_total(marks[1:])

def calculate_average():
    try:
        name = input('Enter student name to calculate average:-')

        if name not in student_marks:
            raise NameError
    
        marks = student_marks[name]
        total = recursive_total(marks)
        average = total/len(marks)
    
        print('Total marks:-',total)
        print('Average marks:-',average)

    except NameError:
        print('Student name not found')


    except ZeroDivisionError:
        print('Cannot divide by zero')

    except TypeError:
        print('Marks data type error')

while True:
    print('1.Add Student')
    print('2.Display Students')
    print('3.Claculate Average')
    print('4.Exit')
    
    try:
        choice = int(input('Enter choice:-'))

        if choice == 1:
            add_students()
        elif choice == 2:
            display_students()
        elif choice == 3:
            calculate_average()
        elif choice == 4:
            print('Thank You!')
            break
        else:
            print('Invalid Choice')

    except ValueError:
        print('Please enter a valid choice number')

