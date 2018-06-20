import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компиляції: ' + str(datetime.datetime.now()))
s = list(map(int,input("Введите количество штучек и штукенций через пробел: ").split()))
print("Общая масса: ",(75 * s[0]) + (112 * s[1]),"грамм")
printTimeStamp("Сергій Михайлов")
