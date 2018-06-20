import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
data = list(map(int,input("Введите промежуток времени в формате ДНИ-ЧАСЫ-МИНУТЫ-СЕКУНДЫ через пробел: ").split()))
print ("Результат в секундах:", (86400 * data[0]) + (3600 * data[1]) + (60 * data[2]) + data[3])
printTimeStamp("Сергій Михайлов")