def checkio(time_string):
    a = list((time_string.replace(':', ' ')).split())
    a[0] = int(a[0])
    a[1] = int(a[1])
    a[2] = int(a[2])
    a[0] = str(("{0:b}".format(a[0] // 10)).zfill(2)) + ' ' + str(("{0:b}".format(a[0] % 10)).zfill(4)) + ' :'
    a[1] = ' ' + str(("{0:b}".format(a[1] // 10)).zfill(3)) + ' ' + str(("{0:b}".format(a[1] % 10)).zfill(4)) + ' :'
    a[2] = ' ' + str(("{0:b}".format(a[2] // 10)).zfill(3)) + ' ' + str(("{0:b}".format(a[2] % 10)).zfill(4))
    a[0] = (a[0]).replace("1", "-").replace("0", ".")
    a[1] = (a[1]).replace("1", "-").replace("0", ".")
    a[2] = (a[2]).replace("1", "-").replace("0", ".")
    return a[0] + a[1] + a[2]
print(checkio('10:37:49'))