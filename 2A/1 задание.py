import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Давлат Черновол')
lst = [0,1,2,3,4,5,6,7,8,9,100,2,4,6,7,4,2,1,0]
lis3=list(set(lst))
print (lis3)
lst2=lst[:]
a=lst2[0]
b=lst2[2]
c=lst2[3]
lst2.remove(a)
lst2.remove(b)
lst2.remove(c)
print(lst2)
