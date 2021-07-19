#handeling errors in python program
try:   #here we are telling pthon to try the following code
    age = int(input("Enter age:- "))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:  #now it will handle this typr of error to and will display the below code
    print('Age cannot be zero')
except ValueError:   #if any error of type ValueError occurs then do the following code.
    print('Invalid Entry')
