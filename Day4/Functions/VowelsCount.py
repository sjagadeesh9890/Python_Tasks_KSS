def count_vowels(string):
    count =0
    vowels = 'AEIOUaeiou'

    for char in string:
        if char in vowels:
            count +=1

    return count

string = input('enter a string')
print(count_vowels(string))
