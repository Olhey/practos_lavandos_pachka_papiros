import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
a = list(map(int,input("Введите дату в формате MM/DD через пробел: ").split()))
if (a[0] == 12 and a[1] >= 22) or (a[0] == 1 and a[1] <= 19):
    print("Carpicorn")
elif (a[0] == 1 and a[1] >= 20) or (a[0] == 2 and a[1] <= 18):
    print("Aquarius")
elif (a[0] == 2 and a[1] >= 19) or (a[0] == 3 and a[1] <= 20):
    print("Pisces")
elif (a[0] == 3 and a[1] >= 21) or (a[0] == 4 and a[1] <= 19):
    print("Aries")
elif (a[0] == 4 and a[1] >= 20) or (a[0] == 5 and a[1] <= 20):
    print("Taurus")
elif (a[0] == 5 and a[1] >= 21) or (a[0] == 6 and a[1] <= 20):
    print("Gemini")   
elif (a[0] == 6 and a[1] >= 21) or (a[0] == 7 and a[1] <= 22):
    print("Cancer")  
elif (a[0] == 7 and a[1] >= 23) or (a[0] == 8 and a[1] <= 22):
    print("Leo") 
elif (a[0] == 8 and a[1] >= 23) or (a[0] == 9 and a[1] <= 22):
    print("Virgo")
elif (a[0] == 9 and a[1] >= 23) or (a[0] == 10 and a[1] <= 22):
    print("Libra")
elif (a[0] == 10 and a[1] >= 23) or (a[0] == 11 and a[1] <= 21):
    print("Scorpio")
elif (a[0] == 11 and a[1] >= 22) or (a[0] == 12 and a[1] <= 21):
    print("Sagittarius")
printTimeStamp("Давлат Черновол")
