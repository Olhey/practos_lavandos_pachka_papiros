import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

def factorial(n):
    if n==0:
        return 1
    else :
        a=factorial(n-1)*n
        return a

print(factorial(5))
printTimeStamp("Сергій Михайлов")