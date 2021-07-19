# guessing game ....while loop

num_try = 1
while num_try <= 3:
    crct_num = 8
    num_try = num_try + 1
    guess_num = int(input('Guess : '))
    if crct_num == guess_num:
        print('You win :D')
        break
else:
    print('You failed !!')


