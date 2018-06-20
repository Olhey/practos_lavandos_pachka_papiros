import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a=int(input("How many minutes did you spend on talking?"))
b=int(input("How many times did you send sms?"))

result=(a-200)*float(0.17)+(b-50)*float(0.15)+15
result2=result+15*float(0.05)+float(0.44)
print("Check without taxes - "+str(result))
print("Check with taxes - "+str(result2))
printTimeStamp("Сергій Михайлов")