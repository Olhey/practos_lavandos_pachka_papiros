import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

def HCD(x,y):
    if y==0:
       return x
    else:
       return HCD(y, x % y)
print(HCD(16,20))
printTimeStamp("Давлат Черновол")
