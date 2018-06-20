import datetime
import math
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
a = list(map(int,input("Введите длинну (в см) и количество сторон через пробел: ").split()))
print("Площа построенного полигона: ", (a[1] * math.pow(a[0], 2)) / math.tan(4) * (math.pi / a[1]))
printTimeStamp("Сергій Михайлов")