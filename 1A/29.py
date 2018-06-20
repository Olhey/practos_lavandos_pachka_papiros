import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

n=1
p=30
for row in range(2):
    print(" "*p+"xxx"*n)
    n+=2
    p-=3
    if n==5:
        n=13
        p+=1

        for row in range(3):
            print(" " * p + "x" * n)
            n+=2
            p-=1

            if n == 17:
                print(" " * p + "x" * n)
                for row in range(3):
                 print(" " * p + "x" * n)
                 n-=2
                 p+=1

                 for row in range(1):
                     if n ==11:
                         n=3
                         p = 27
                         print(" " * p + "xxx" * n)
                         p+=3
printTimeStamp("Сергій Михайлов")