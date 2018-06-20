import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a=input("Numbers:")
if isinstance(a[0:2],str) and a[3:5].isdigit()  and a[0:3].isupper():
    print("You have obsolete version of the machine number")
elif a[0:3].isdigit() and isinstance(a[4:6],str)and a[4:6].isupper():
    print("You have new version of the machine number")
else:
    print("Error!!!")
printTimeStamp("Давлат Черновол")
