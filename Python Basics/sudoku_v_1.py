table = '''
 _______________
|_3_|_A_|_D_|_2_|
|_B_|_4_|_1_|_C_|
|_1_|_H_|_2_|_F_|
|_G_|_2_|_E_|_1_|
'''
print()
print('This is Sudoko Game. Enter the correct value of A, B, C, D, E, F, G and H to win the game.')
print('Below is the Table:-')
print(table)
print()
i = 0
while i == 0:
    num = int(input('Enter the value of A: '))
    if num == 1:
        print('The Value of A is Correct')
        print('''
         _______________
        |_3_|_1_|_D_|_2_|
        |_B_|_4_|_1_|_C_|
        |_1_|_H_|_2_|_F_|
        |_G_|_2_|_E_|_1_|
        ''')
        break
    else:
        print('The value of A is wrong!')
        i = 0
i = 0
while i == 0:
    num = int(input('Enter the value of B: '))
    if num == 2:
        print('The Value of B is Correct')
        print('''
                 _______________
                |_3_|_1_|_D_|_2_|
                |_2_|_4_|_1_|_C_|
                |_1_|_H_|_2_|_F_|
                |_G_|_2_|_E_|_1_|
                ''')
        break
    else:
        print('The value of B is wrong!')
        i = 0
i = 0
while i == 0:
    num = int(input('Enter the value of C: '))
    if num == 3:
        print('The Value of C is Correct')
        print('''
                 _______________
                |_3_|_1_|_D_|_2_|
                |_2_|_4_|_1_|_3_|
                |_1_|_H_|_2_|_F_|
                |_G_|_2_|_E_|_1_|
                ''')
        break
    else:
        print('The value of C is wrong!')
        i = 0
i = 0
while i == 0:
    num = int(input('Enter the value of D: '))
    if num == 4:
        print('The Value of D is Correct')
        print('''
                 _______________
                |_3_|_1_|_4_|_2_|
                |_2_|_4_|_1_|_3_|
                |_1_|_H_|_2_|_F_|
                |_G_|_2_|_E_|_1_|
                ''')
        break
    else:
        print('The value of D is wrong!')
        i = 0
i = 0
while i == 0:
    num = int(input('Enter the value of E: '))
    if num == 3:
        print('The Value of E is Correct')
        print('''
                     _______________
                    |_3_|_1_|_4_|_2_|
                    |_2_|_4_|_1_|_3_|
                    |_1_|_H_|_2_|_F_|
                    |_G_|_2_|_3_|_1_|
                        ''')
        break
    else:
        print('The value of E is wrong!')
        i = 0
i = 0
while i == 0:
    num = int(input('Enter the value of F: '))
    if num == 4:
        print('The Value of F is Correct')
        print('''
                     _______________
                    |_3_|_1_|_4_|_2_|
                    |_2_|_4_|_1_|_3_|
                    |_1_|_H_|_2_|_4_|
                    |_G_|_2_|_3_|_1_|
                        ''')
        break
    else:
        print('The value of F is wrong!')
        i = 0
i = 0
while i == 0:
    num = int(input('Enter the value of G: '))
    if num == 4:
        print('The Value of G is Correct')
        print('''
                     _______________
                    |_3_|_1_|_4_|_2_|
                    |_2_|_4_|_1_|_3_|
                    |_1_|_H_|_2_|_4_|
                    |_4_|_2_|_3_|_1_|
                        ''')
        break
    else:
        print('The value of G is wrong!')
        i = 0
i = 0
while i == 0:
    num = int(input('Enter the value of H: '))
    if num == 3:
        print('The Value of H is Correct')
        print('''
                     _______________
                    |_3_|_1_|_4_|_2_|
                    |_2_|_4_|_1_|_3_|
                    |_1_|_3_|_2_|_4_|
                    |_4_|_2_|_3_|_1_|
                        ''')
        break
    else:
        print('The value of H is wrong!')
        i = 0
print('(: CONGRATULATIONS BUDDY YOU MADE IT THROUGH :)')