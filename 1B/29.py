import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
def function(n):
  factors = []
  d = 2
  m = n
  if (m < d):
    print("Error!!")
    return 0
  else:
    while (d * d <= n) and (m >= 2):
     if n % d == 0:
       factors.append(d)
       n //= d
     else:
      d += 1
      factors.append(n)
      print(m," = ",factors)
n = int(input("Number:"))
function(n)
printTimeStamp("Давлат Черновол")
