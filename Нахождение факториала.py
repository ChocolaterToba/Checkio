while True:
    try:
        print('Input your number')
        number = int(input())
        output = number
        while number > 1 :
            output = number * output
            number = number - 1
        print("That number's factorial is ", output)
    except ValueError:
        print('You have inputed a letter. Try again') 