import datetime
import random

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


b=[]
def generator():
    for i in range(3):
        a =( "380(" + str(random.randint(10,20))+")-"+str(random.randint(111,999)) +"-"+ str(random.randint(10,20))+"-" + str(random.randint(10,20)))
        b.append(a)
generator()
print(b)
printTimeStamp("Сергій Михайлов")