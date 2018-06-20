import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = str(input("Введите название месяца с большой буквы: "))
if name == "Сентябрь" or name == "Ноябрь" or name == "Июнь" or name == "Апрель":
    print("В данном месяце 30 дней")
elif name == "Февраль":
    print("В данном месяце 28 или 29 дней")
else:
    print("В данном месяце 31 день")
printTimeStamp("Сергій Михайлов")
