import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
result = ""
q = int(input("Введите число: "))
while (q != 0):
    r = q%2
    result += str(r)
    q = q//2
print(result[::-1])
printTimeStamp("Сергій Михайлов")