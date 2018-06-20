import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

money=int(input("Money:"))
first_year=money*(1+float(0.14)*1)
second_year=money*(1+float(0.14)*2)
third_year=money*(1+float(0.14)*3)
print("First year "+"%2.f"%(first_year)+"\n"+"Second year "+"%2.f"%(second_year)+"\n"+"Third year "+"%2.f"%(third_year)+"\n")
printTimeStamp("Сергій Михайлов")