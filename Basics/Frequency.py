# Frequency Counter: Given a string `"programming"`, create a dictionary that counts how many times each character appears.
 
# Expected output:
 #{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1,'m': 2, 'i': 1, 'n': 1}
string = 'programming'
freq = {}
for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)
