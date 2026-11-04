# Write a program to remove duplicate elements from a list.
  li = [1,2,2,3,4,5,6,6,7,34,44,6,44,10,10,10,10] #Actual list
  lis = [] #Storing in a new list without duplicate values
  for num in lis:  #Checking every number in a list
      if num not in lis: # if a number already exists it is not adding again that number
          lis.append(num)  # A number is adding ina new list 
  print(lis)  # this is the result without dupicate numbers with new list
