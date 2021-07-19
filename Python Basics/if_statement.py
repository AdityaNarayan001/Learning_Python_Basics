print('************IF STATEMENT*************')
is_hot = False
is_cold = False
if is_hot:
    print('It is a hot day')
    print('Drink plenty of water')
elif is_cold:
    print('It is cold day')
    print('Dont go out')
else:
    print('Its a lovely day')
print('Enjoy Your Day')
print('******************TASK********************')
print('The house is worth 1M or 1000000lac')
house = 1
credit_good = True
if credit_good:
    down_payment = house * (10/100)
    msg = f'Your Down Payment is {down_payment} M'
    print(msg)
else:
    down_payment2 = house * (20/100)
    msg2 = f'Your Down Payment is {down_payment2} M'
    print(msg2)
