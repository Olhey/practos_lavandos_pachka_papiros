import datetime
import random

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a=list(map(int, input("Numbers:").split()))
b=[1,3,1,3,1,3,1,3,1,3,1,3]
s = list(map(lambda x, y: x * y, a, b))
print(sum(s))
Check_digit = 10-(sum(s) % 10)
print(Check_digit)
printTimeStamp("Сергій Михайлов")