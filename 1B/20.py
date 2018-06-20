import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
y= int(input())
x= str(input())
if x=="a":
    x=1
elif x=="b":
    x=2
elif x=="c":
    x=3
elif x=="d":
    x=4
elif x=="e":
    x=5
elif x=="f":
    x=6
elif x=="g":
    x=7
elif x=="h":
    x=8
else:
    print("\nВведенні дані не коректні (виходять за межі дошки)")

if 1<=y<=8:
    if (x+y) % 2 == 0:
        print('Black')
    else:
        print('White')
else:
    print("\nВведенні дані не коректні (виходять за межі дошки)")
printTimeStamp("Сергій Михайлов")