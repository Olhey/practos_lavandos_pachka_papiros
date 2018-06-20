import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

def taxi(lenght):
    pay=25+2*(lenght/140)
    print("You need to pay "+str(int(pay))+"$")

taxi(1400)
printTimeStamp("Давлат Черновол")
