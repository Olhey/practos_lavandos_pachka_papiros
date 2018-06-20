import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
year = int(input("Year:"))
a=(year%100==0)
b=(year%400!=0)
c=(year %4!=0)
if a or (b and c):
    print(year,"Regular Year")
else:
    print(year,"Leap year")
printTimeStamp("Сергій Михайлов")