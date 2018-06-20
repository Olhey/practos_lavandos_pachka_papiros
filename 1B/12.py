import math
import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

t1=math.cos(math.radians(float(input("latitude of 1 point: "))))
t2=math.cos(math.radians(float(input("latitude of 2 point: "))))
g1=math.cos(math.radians(float(input("longitude 1 point: "))))
g2=math.cos(math.radians(float(input("longitude 2 point: "))))
dis=6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print("Distance = %.3f"%dis, "km")
printTimeStamp("Давлат Черновол")
