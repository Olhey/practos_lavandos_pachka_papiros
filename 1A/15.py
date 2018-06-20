import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компиляції: ' + str(datetime.datetime.now()))
a=list(map(int,input("Input numbers:").split(" ")))
if a[0]==int(0):
  print("Error , first number can't be 0")
elif int(0) in a:
    print(sum(a)/(len(a)-1))
printTimeStamp("Сергій Михайлов")
