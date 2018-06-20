import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


money = 0
count = 0
while True:
    a = input("Years old:")
    if str(a) == str("-"):
        if count >= 10:
            money = money - money * 0.1
            print("Payment= %.2f" % money)
            break
        else:
            print("Payment= %.2f" % money)
            break
    elif int(a) <= int(3):
        count += 1
    elif int(3) < int(a) < int(12):
        count += 1
        money += float(16.00)
    elif int(12) < int(a) < int(60):
        count += 1
        money += float(25.00)
    elif int(a) >= int(60):
        count += 1
        money += float(18.00)
print(printTimeStamp("Сергій Михайлов"))

