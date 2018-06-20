
import datetime
import math

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

first_point=1015
second_point=719.1
third_point=797.1
p=(first_point+second_point+third_point)/2
square=math.sqrt(p*(p-first_point)*(p-second_point)*(p-third_point))
print("Square of triangle between Lviv ,Odessa and Kharkov = %.2f"%square,"km²")
printTimeStamp("Сергій Михайлов")