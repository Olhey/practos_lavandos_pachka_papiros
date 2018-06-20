import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
x = str(input("Введіть буквенну оцінку: "))
if x == "A+":
    print("Ваша бальна оцінка: >4.0")
elif x == "A":
    print("Ваша бальна оцінка: 4.0")
elif x == "A-":
    print("Ваша бальна оцінка: 3.7")
elif x == "B+":
    print("Ваша бальна оцінка: 3.3")
elif x == "B":
    print("Ваша бальна оцінка: 3.0")
elif x == "B-":
    print("Ваша бальна оцінка: 2.7")
elif x == "C+":
    print("Ваша бальна оцінка: 2.3")
elif x == "C":
    print("Ваша бальна оцінка: 2.0")
elif x == "C-":
    print("Ваша бальна оцінка: 1.7")
elif x == "D+":
    print("Ваша бальна оцінка: 1.3")
elif x == "D":
    print("Ваша бальна оцінка: 1.0")
elif x == "F":
    print("Ваша бальна оцінка: 0")
else:
    print("Буквенна оцінка не передбачена в таблиці")
printTimeStamp("Сергій Михайлов")
