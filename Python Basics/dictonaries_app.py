num = {
    1:'One',
    2:'Two',
    3:'Three',
    4:'Four',
    5:'Five',
    6:'Six',
    7:'Seven',
    8:'Eigth',
    9:'Nine',
    0:'Zero'
}
ph_num = input('Enter a number: ')
for ph_digit in ph_num:
    while True:
        print(num[int(ph_digit)], end=" ")
        break


