import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компиляції: ' + str(datetime.datetime.now()))
pod = list(map(float,input("Укажите рост в сантиметрах и вес в киллограммах через пробел: ").split()))
res = pod[1] / (pod[0] * pod[0])
result = list (str (res))
del result[0], result[0], result[0], result[0] #В результате подсчета ИМТ всегда убираются ноли
result.insert(2, ".")
print ("IMT: ", (''.join(result)))
printTimeStamp(" Сергій Михайлов ")
