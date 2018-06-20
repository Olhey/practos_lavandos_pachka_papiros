import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
day=int(input("Enter day:"))
month=int(input("Enter month:"))
year=(input("Enter year:"))
if str( day*month) == str( year[2:4]):
    print(str(day)+" Day of the "+str(month)+"month of "+str(year) + " will be magical")
printTimeStamp("Давлат Черновол")
