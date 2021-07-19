# write a program to remove duplicates in list
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
for items in numbers:
    if numbers.count(items)>1:
        numbers.remove(items)
print(numbers)
