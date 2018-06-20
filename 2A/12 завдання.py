import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Сергей Михайлов")

import winsound
import itertools as i

x=[[(440), (440), (440), (349), (523), (440), (349),
(523), (440), (659), (659), (659), (698), (523),
(415), (349), (523), (440)],[(500), (500), (500), (350), (150), (500), (350),
(150), (1000), (500), (500), (500), (350), (150),
(500), (350), (150), (1000)]]
n=0
for item in i.count(1):
    n=n+1
    if n>=18:
        break
    else:
        g=x[0][1]+x[0][n]
        f=x[1][1]+x[1][n]

    winsound.Beep(g,f)
