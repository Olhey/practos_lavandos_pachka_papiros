import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


day=input("Day off or Holidays:")
if day =="Day off":
    List= ("Saturday" ,"Sunday")
    fd = input("Enter day:")
    if fd in List:
        print("Alarm clock off")
    else:
        print("This isn't weekends")
elif day=="Holidays":
    hr=list(input("Enter your vacation days:").split(" "))
    print("Alarm will be disabled in "+",".join(hr))
else:
    print("Try again")
printTimeStamp("Сергій Михайлов")