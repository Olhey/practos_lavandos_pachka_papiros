import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

bread=int(input("Number :"))
cb=bread*float(8.50)
db=bread*float(8.50)*float(0.6)
d=cb-db
print( '%32s %38s %0s %37s' % ("Cost of order without discount - "+"%.2f"%cb+"\n","Discount - "+"%.2f"%d+"\n","-"*37+"\n","Cost of order - "+"%.2f"%db) )
printTimeStamp("Сергій Михайлов")