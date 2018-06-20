import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Давлат Черновол")

lis = [1]
def Catalan(n):
    global lis
    while(len(lis) != n+1):
        lis.append(int(int(lis[len(lis)-1] ) * (4*len(lis)-2)/(len(lis)+1) ) )
    print(lis[n])
k=int(input("Введіть число: "))
Catalan(k)
