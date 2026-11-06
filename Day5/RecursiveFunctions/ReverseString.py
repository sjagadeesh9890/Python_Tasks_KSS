# Write a recursive function to reverse a string.
def reverse_string(s):
      if s == '':
          return s
      else:
          return reverse_string(s[1:])+s[0]

s = 'jagadeesh'
print(reverse_string(s))
