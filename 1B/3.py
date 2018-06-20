import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
i=0
f=32
for row in range(11):
    print(str(i)+" C = "+str(f)+"F")
    i += 10
    f = i *float(9/5)+32
printTimeStamp("Сергій Михайлов")