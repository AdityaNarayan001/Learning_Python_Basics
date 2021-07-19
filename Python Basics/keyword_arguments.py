#we have positional arguments as well as we can define arguments

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome aboard')

print('Start')
greet_user(last_name='Smith',first_name='John')
print('Finish')