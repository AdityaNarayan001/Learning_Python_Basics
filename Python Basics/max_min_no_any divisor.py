print()
print('Find Greatest or Smallest number of any number of Digits divisible by number of your wish.')
while True:
    segment = input('Type "Great" for Greatest Number calculation and "Small" for Smallest Number calculation and Exit to quit:-  ')
    if segment.upper() == 'GREAT':
        g_num_order = int(input('Greatest number of how many digits:- '))
        divisor = input('Enter the number by which it should be divisible:- ')
        g_num = '9'* int(g_num_order)
        process = int(g_num) % int(divisor)
        result = int(g_num) - process
        statement = f'The Greatest {g_num_order} digit number divisible by {divisor} is {result}'
        print(statement)
    elif segment.upper() == 'SMALL': #here is some error with s_divisor input as 10
        s_num_order = int(input('Smallest number of how many digits:- '))
        s_divisor = input('Enter the number by which it should be divisible:- ')
        s_num = 10**(int(s_num_order))
        process = int(s_num) % int(s_divisor)
        s_result = (s_num - process) + int(s_divisor)
        sec_statement = f'The Smallest {s_num_order} digit number divisible by {s_divisor} is {s_result}'
        print(sec_statement)
    elif segment.upper() == 'EXIT':
        break
    else:
        print("Didn't get you man !!")
print('Thank You')