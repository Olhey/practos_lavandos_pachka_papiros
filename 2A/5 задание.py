import operator
import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Давлат Черновол')
x = {1: 6, 3: 4, 4: 3, 2: 1, 0: 0,5:1,100:0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))
sorted_x_r = sorted(x.items(), key=operator.itemgetter(0),reverse=True)
print(sorted_x)
print(sorted_x_r)

print(sorted_x+sorted_x_r)
