print('*************STRINGS***************')
print('Sometimes we use single and double quotes in combination to get our job done')
print("Python's a course for Begginners")
print('Python for "Begginners"')
email = '''
Hi John,
This is our first email to you.

Thank you
The Support Team

'''
print(email)
print('***********MORE PROPERTIES OF STRINGS**************')
course = 'Python for Beginners'
print(course[0])
print(course[-1])
print('The above example is of index where the square bracket carries the index number of string in course')
print(course[0:4])
print('The above prints all char from index 0 to 3rd index')
print(course[0:])
print(course[1:])
print(course[:5])
another = course[:]
print(another)
name = 'Aditya'
print(name[1:-1])