import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Давлат Черновол")

import random
red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
rand= [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35,1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36,"0", "00"]
word= random.choice(rand)
print("На рулетці випало: ", word)
for i in range(1):
    if word == "0":
        print("Виплатити:", word)
        break
    if word == "00":
        print("Виплатити:", word)
        break
    print("Виплатити:", word)
    if word in red:
        print("Виплатити:", "red")
    if word in black:
        print("Виплатити:","black")
    if word%2:
        print("Виплатити:","Odd")
    else:
        print("Виплатити:","Even")
    if 1<=word<=18:
        print("Виплатити:","1 to 18")
    if 19<=word<=36:
        print("Виплатити:","19 to 36")

