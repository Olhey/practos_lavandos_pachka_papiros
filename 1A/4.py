import datetime

def printTimeStamp(name):
    def printTimeStamp(name):
        print('Автор програми: ' + name)
        print('Час компиляції: ' + str(datetime.datetime.now()))
a=input(" Letter :")
if  a == "a" or a == "i" or a == "e" or a == "o" or a == "u": print("The letter is vowel.")
elif a=="y": print("Y - vowel, and sometimes - consonant")
else: print("The letter is consonant")
printTimeStamp("Сергій Михайлов")