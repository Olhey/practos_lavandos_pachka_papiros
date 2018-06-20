import datetime
import math
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
a = list(map(int,input("Введите два числа через пробел: ").split()))
print("Сложение: ", a[0]+a[1] ,"\nВычитание b-a: ", a[1]-a[0], "\nУмножение: ", a[0]*a[1], "\nОстаток при делении: ", a[0]%a[1], "\nДеление: ", a[0]/a[1], "\nЗначение log10:", math.log10(a[0]), "\nВозведение a в степень b: ", math.pow(a[0], a[1]))
printTimeStamp("Сергій Михайлов")