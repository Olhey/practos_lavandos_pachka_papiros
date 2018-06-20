import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name=str(input("Print your name: "))
print("Hello,"+name)
printTimeStamp(" Сергій Михайлов ")