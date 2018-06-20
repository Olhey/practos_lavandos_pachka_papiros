import datetime
import time

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

print("%s"%time.asctime())
printTimeStamp("Сергій Михайлов")