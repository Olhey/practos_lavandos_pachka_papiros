import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a=(F(n-1)+F(n-2))
        return(a)
print(F(8))
printTimeStamp("Сергій Михайлов")