import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a=float(input(":"))
if a <=float(2.0) :
    print("Micro earthquake")
elif a <=float(3.0):
    print("Very minor earthquake")
elif a <=float(4.0):
    print("Minor earthquake")
elif a <=float(5.0):
    print("Light earthquake")
elif a <=float(6.0):
    print("Moderate earthquake")
elif a <=float(7.0):
    print("Strong earthquake")
elif a <=float(8.0):
    print("Major earthquake")
elif a <=float(10.0):
    print("Great earthquake")
elif a >float(10.0):
    print("Meteoric earthquake")
printTimeStamp("Сергій Михайлов")
