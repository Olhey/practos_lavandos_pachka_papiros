import datetime
def printTimeStamp(name):
    print('Автори програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a=input("Numbers:")
b=list(a)
c="+".join(b)
print(str(int(b[0])+int(b[1])+int(b[2])+int(b[3]))+"="+str(c))
printTimeStamp("Сергій Михайлов")