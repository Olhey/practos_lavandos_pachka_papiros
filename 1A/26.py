import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a=(input("Sides: ")).split()


if a[0]==a[1]==a[2]:
    print("Рівносторонній трикутник")
elif a[0]==a[1]!=a[2]:
    print("Рівнобедрений трикутник")
else:
    print("Нерівносторонній триркутник")
printTimeStamp("Сергій Михайлов")