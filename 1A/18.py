import datetime
import math
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
d = int(input("Укажите высоту падения в метрах: "))
print("Конечная скорость: ", math.sqrt((96.04 * d) * 2), "м/с")
printTimeStamp("Сергій Михайлов")