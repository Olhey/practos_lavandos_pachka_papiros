import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
x=float(input("Введіть  рівень гучності в dB: "))

if x == 40:
    print("Jackhammer")
elif 40 < x < 70:
    print("Шум знаходиться між Jackhammer і Gas lawnmower")
elif x == 70:
    print("Gas lawnmower")
elif 70 < x < 106:
    print("Шум знаходиться між Gas lawnmower і Alarm clock")
elif x == 106:
    print("Alarm clock")
elif 106 < x < 130:
    print("Шум знаходиться між Alarm clock і Quiet room")
elif x == 130:
    print("Quiet room")
else:
    if x<40:
        print("Введений шум, нижчий за найтихіший шум")
    else:
        print("Введений шум, вищий за найвищий шум")
printTimeStamp("Сергій Михайлов")
