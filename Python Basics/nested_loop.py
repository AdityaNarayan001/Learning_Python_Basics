for x in range(3):
    for y in range(3):
        print(f'({x}, {y})')

print()
numbers = [1, 1, 1, 1, 5]
for num in numbers:
    output = ''
    for count in range(num):
        output += 'x'
    print(output)