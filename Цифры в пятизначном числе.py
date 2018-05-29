while True:
    try:
        first_input = int(input('Press [1] to continue or [2] to exit: '))
        if first_input == 1:
            a = int(input('Input your 5-digit number : '))
            first_number = a // 10000
            a = a - 10000 * first_number
            second_number = a // 1000
            a = a - 1000 * second_number
            third_number = a // 100
            a = a - 100 * third_number
            fourth_number = a // 10
            fifth_number = a % 10
            print('First number is: ', first_number)
            print('Second number is: ', second_number)
            print('Third number is: ', third_number)
            print('Fourth number is: ', fourth_number)
            print('Fifth number is: ', fifth_number)
        elif first_input == 2:
            break
    except ValueError:
        print('Your input is invalid')
        