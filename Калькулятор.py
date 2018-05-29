while True:   
    print('Choose your option (By inputing number):')
    print('Addition[1]')
    print('Substraction[2]')
    print('Multiply[3]')
    print('Divide[4]')
    print('Exit[5]')
    input_user = input()
    #Checking for quiting input
    if input_user == '5':
        break
    if input_user == '1':
        try:
            print('Input 2 numbers')
            user_input1 = input()
            user_input2 = input()
            result = float(user_input1) + float(user_input2)
            if result - int(result) == 0:
                print(int(result))
            else:
                print(result)
             
            #Check for a typo
        except ValueError:
            print('Invalid input. Probably a letter.')
            print(' ')
    elif input_user == '2':
        try:
            print('Input 2 numbers')
            user_input1 = input()
            user_input2 = input()        
            result = float(user_input1) - float(user_input2)
            if result - int(result) == 0:
                print(int(result))
            else: 
                print(result)
        except ValueError:
            print('Invalid input. Probably a letter.')
            print(' ')
    elif input_user == '3':
        try:
            print('Input 2 numbers')
            user_input1 = input()
            user_input2 = input()         
            result = float(user_input1) * float(user_input2)
            if result - int(result) == 0:
                print(int(result))
            else: 
                print(result)
        except ValueError:
            print('Invalid input. Probably a letter.')
            print(' ')
    elif input_user == '4':
        try:
            print('Input 2 numbers')
            user_input1 = input()
            user_input2 = input()             
            result = float(user_input1) / float(user_input2)
            if result - int(result) == 0:
                print(int(result))
            else: 
                print(result)
        #Just so program won't bug if user inputs 0
        except ZeroDivisionError:
            print('Cannot divide by zero')
            print(' ')
        except ValueError:
            print('Invalid input. Probably a letter.')
            print(' ')
    #Finally, check for other imputs
    else:
        print('Wrong input. Try again')
        print(' ')