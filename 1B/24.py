import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))





num=float(input("Number:"))
deg=int(input("Degree of 10:"))
a=num*10**deg
print(str(int(a))+" Hz")
if a < int(3*10**9) :
    print("Radio waves")
elif int(3*10**9) <= a < int(3*10**12):
    print("Microwaves")
elif int(3*10**9)<= a <int(4.3*10**14):
    print("Infared light")
elif int(4.3*10**14) <= a <int(7.5*10**14):
    print("Visible light")
elif int(7.5*10**14) <= a <int(3*10**17):
    print("Ultraviolent light")
elif  int(3*10**17) <= a < int(3*10**19):
    print("X-rays")
elif  int(3*10**19)<= a :
    print("Gamma rays")
printTimeStamp("Сергій Михайлов")