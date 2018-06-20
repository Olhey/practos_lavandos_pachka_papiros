def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
sm = float(input("Введите свой рост в сантиметрах: "))
print("Дюймы: ",sm / 2.54 , "\nФуты: ", sm / 30.48)
printTimeStamp("Сергій Михайлов")