def my_funk(x):
    for i in range(0, x + 1):
        yield i
print('Input your number')
x = int(input())
print(list(my_funk(x)))
    
    