from Calculator import*
print('Calculator Program \n1.Addition \n2.Substraction \n3.Multiplication \n4.Division')
choice = int(input('Enter your choice(1-4):-'))
number1 = float(input('Enter first number-'))
number2 = float(input('Enter second number:-'))
if choice == 1:
    result = add(number1,number2)
    print('Result:-',result)

elif choice == 2:
    result = substract(number1,number2)
    print('Result:-',result)

elif choice == 3:
    result = multiply(number1,number2)
    print('Result:-',result)

elif choice == 4:
    result = divide(number1,number2)
    print('Result:-',result)

else:
    print('Invalid choice!')
