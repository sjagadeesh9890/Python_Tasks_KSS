# Write a program to find the second largest number in a list.
  li = [0,1,2,3,4,5,6,7,8,9]
  lis = list(set(li))  #set() is using to remove duplicate values in a list
  lis.sort()
  print(lis[-2])
