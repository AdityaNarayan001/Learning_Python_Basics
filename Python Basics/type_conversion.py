print('***********TYPE CONVERSION*************')
print('type() it is a function that tell the type of variable entered between the ()')
birth_year = input('Enter Your Birth Year: ')
current_year = input('Enter Current Year: ')
age = int(current_year) - int(birth_year)
print('You are ' + str(age) + ' years old.')
print(type(birth_year))
print(type(age))
print('****************TASK*****************')
kg_weight = input('Enter your Weight in Kg: ')
gm_weight = 1000 * float(kg_weight)
print('You are ' + str(gm_weight) + 'grams')