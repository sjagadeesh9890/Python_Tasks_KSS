# Remove Duplicates: Given a list `[1, 2, 3, 2, 4, 1, 5, 3]`, remove duplicate elements while preserving the original order. Do not use `set()`.
lis = [1,2,3,2,4,1,5,3]
duplicate = []

for num in lis:
    if num not in duplicate:
        duplicate.append(num)
print(duplicate)
