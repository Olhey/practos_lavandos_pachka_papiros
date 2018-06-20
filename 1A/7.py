import datetime
def printTimeStamp(name):
    print('Автори програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
c = float(input("Температура в градусах Цельсия: "))
print("В Фаренгейтах: ",(c * (9/5)) + 32," градуса","\nВ Кельвинах: ",273.15 + c," градуса")
printTimeStamp("Сергій Михайлов")
