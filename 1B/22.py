import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")


a=list(map(float,input("Введіть числа:").split(" ")))

if int(-1) in a:
    x=(sum(a)+1)/(len(a)-1)
    print("Середня оцінка по групі: ",x)
    if 5.0 >=x > 4.0:
        print("Ваша бальна оцінка: A+")
    elif 4.0 >= x > 3.7:
        print("Ваша бальна оцінка: A")
    elif 3.7 >= x > 3.4:
        print("Ваша бальна оцінка: A-")
    elif 3.4 >= x > 3.0:
        print("Ваша бальна оцінка: B+")
    elif 3.0 >= x > 2.7:
        print("Ваша бальна оцінка: B")
    elif 2.7 >= x > 2.4:
        print("Ваша бальна оцінка: B-")
    elif 2.4 >= x > 2.0:
        print("Ваша бальна оцінка: C+")
    elif 2.0 >= x > 1.7:
        print("Ваша бальна оцінка: C")
    elif 1.7 >= x > 1.4:
        print("Ваша бальна оцінка: C-")
    elif 1.4 >= x > 1:
        print("Ваша бальна оцінка: D+")
    elif 1 >= x > 0:
        print("Ваша бальна оцінка: D")
    elif x==0:
        print("YOU STUPID, PROSTITE ")
    else:
        print("Буквенна оцінка не передбачена в таблиці")
printTimeStamp("Сергій Михайлов")