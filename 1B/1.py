import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

P=int(input("Tension:"))
V=int(input("Volume:"))
t=int(input("Temperature:"))
n=P*V/float(8.314)*float(t+273.15)
print(n)
printTimeStamp("Сергій Михайлов")