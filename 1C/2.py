import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
a = list(map(int,input("Введите дату в формате YEAR/MONTH/DAY через пробел: ").split()))
d = datetime.date(a[0], a[1], a[2])
print (d + datetime.timedelta(days = 1))
printTimeStamp("Давлат Черновол")
