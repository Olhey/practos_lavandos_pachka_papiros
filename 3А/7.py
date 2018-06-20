import datetime
import random

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


b=[]

def pas_gen(lenght):
   count = 0
   for n in range(lenght):
    for i in range(random.randint(8,16)):
        a=(chr(random.randint(33,126)))
        b.append(a)
    count+=1
    b.append(" - " +str(count)+" Password"+"\n")
pas_gen(10)
print("".join(b))
printTimeStamp("Давлат Черновол")
