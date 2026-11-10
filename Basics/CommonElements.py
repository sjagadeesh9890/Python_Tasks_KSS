# Common Elements Using Sets: Given two lists:
    # list1 = [1, 2, 3, 4, 5]
    # list2 = [3, 4, 5, 6, 7]
    # Find:
    # Common elements.
    # Elements present only in the first list.
    # All unique elements from both lists.
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

set1 = set(list1)
set2 = set(list2)
print(set1.intersection(set2))    #we can write in this way also set1 & set2
print(set1.difference(set2))      #we can write in this way also set1 - set2
print(set1.symmetric_difference(set2))  #we can write in this way also set1 &^ set2
