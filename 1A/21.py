import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
a = int(input("Введите целое число: "))
print("Сумма всех числел: ", (a * (a + 1)) / 2)
printTimeStamp("Сергій Михайлов")
