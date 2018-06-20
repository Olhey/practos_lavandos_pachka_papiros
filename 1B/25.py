import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


water = int(input("Water:"))
money = 20
if water<=30:
    money+=float(water*9.86)
elif 30<water<=50:
    money+=float((water-30)*11.22+295.8)
elif 50<water<=60:
    money += float((water - 50) * 13.06+520.2)
elif water>60:
    money+=float((water-60)*17.89+652.8)
print("Счёт за воду:"+"\n"+str(water)+" м3 = "+str(money)+"₴")
printTimeStamp("Сергій Михайлов")



