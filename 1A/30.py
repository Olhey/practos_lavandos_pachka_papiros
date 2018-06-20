import datetime
import math

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
M=float(input("weight of egg:"))
To=int(input("Temperature of egg:"))
t=((M**float(2/3))*float(3.7)*(float(1.038)**float(1/3)))/ 5400*(math.pi**2)*(4*math.pi/3)**(2/3)*math.log10(0.76*((To-100)/(70-100)))
t=t*60
print("%.2f"%t)
printTimeStamp("Сергій Михайлов")