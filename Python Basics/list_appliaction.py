num = [1, 2, 3, 4, 5, 6, 7]
print(max(num))

numbers = [1, 2, 3, 4, 5, 6, 7]
max = numbers[0]
for num in numbers:
    if num > max:
        max = num
print(num)