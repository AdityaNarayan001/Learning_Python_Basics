temp = int(input('Enter Todays temperature in Celsius :- '))
if temp >= 30:
    print('Its a Hot Day')
elif temp <= 10:
    print('It is a cold day')
else:
    print('Its not hot nor cold')

#other example

name = input('Enter your Name : ')
if len(name) < 3:
    print('Name must have atleast 3 char')
elif len(name) > 50:
    print('name should have less than 50 char')
else:
    print('Name looks good')