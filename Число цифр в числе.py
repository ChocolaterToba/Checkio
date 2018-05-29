def checkio(*args, sep = " "):
    if args:    
        for x in args:
            a = list(x)
        return min(a)
    else:
        return 0    

print(checkio(1, 2, 3))