import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

t=float(input("ºС:"))
w=float(input("Wind speed: "))
if t<=10 and w>4.8:
    WCI = (13.12 + 0.6215*t-11.37*(w**0.16)+0.3965*t*(w**0.16))
    print("Wind chill index): %.f"%WCI)
else:
    print("Error!!! \nTemperature must be lower than 10ºС ,wind speed must be bigger than 4.8kph")
printTimeStamp("Сергій Михайлов")