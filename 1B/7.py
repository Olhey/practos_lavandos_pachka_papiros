import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


a=input("Місце проживання:")
b=int(input("Час вдома:"))
print("Ми пропонуємо вам завести :")
if a=="Будинок" and b>=18:
    print("В’єтнамське порося")
elif a == "Будинок" and 10< b <17 :
    print("Собаку")
elif a == "Будинок" and b <10:
    print("Змію")
elif a == "Квартира" and b >10 :
    print("Кішку")
elif a == "Квартира" and b <10 :
    print("Хом’яка")
elif a == "Гуртожиток" and b >6:
    print("Рибку")
elif a == "Гуртожиток" and b < 6 :
    print("Мурашник")
printTimeStamp("Сергій Михайлов")

