import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

d=0
h=0
m=0
time=int(input("Time:"))
a=time
while time>=86400:
    time-=86400
    d+=1
while time>=3600:
    time-=3600
    h+=1
while time>=60:
    time-=60
    m+=1
print(str(a)+" seconds = {} days , {} hours , {} minutes , {} seconds".format(d,h,m,time))
printTimeStamp("Сергій Михайлов")