import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

year=int(input("Year:"))
if "-" in str(year) :print("Try again")
elif int(year) ==int(1):
    print(str(year)+" year of human life = 10.5 years of dog life ")
else:
  dog_years=(((year-2)*4)+21)
  print(str(year)+" years of human life = "+str(dog_years)+" years of dog life ")
printTimeStamp("Сергій Михайлов")