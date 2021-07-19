# car game while loop aplication**************GREAT EXAMPLE****************
print("Type HELP to learn more")
started = False
while True:
    user_cmd = input("Type here :- ")
    comp_cmd = user_cmd.upper()
    if comp_cmd == 'HELP':
        print('START --> To start the car')
        print('STOP --> To stop the car')
        print('QUIT --> To Quit the game')
    elif comp_cmd == 'START':
        if started:
            print('Car is already started !!')
        else:
            started = True
            print('Car started ....ready to go')
    elif comp_cmd  == 'STOP':
        if started is not True:
            print('Car is already at stop')
        else:
            started = False
            print('Car stopped .....')
    elif comp_cmd == 'QUIT':
        print('Thanks for playing')
        break
    else:
        print('I didnt get that....')

