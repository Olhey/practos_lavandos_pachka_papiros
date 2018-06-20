import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Давлат Черновол")

x=list(map(str,input()))
myset=set(x)
print(myset)
