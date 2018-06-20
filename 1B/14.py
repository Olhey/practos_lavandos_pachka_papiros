import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
a = int(input('Введите год:'))
if a == 2000 or a == 2012 or a == 2024:
  print('Дракон')
elif a == 2001 or a == 2013 or a == 2025:
  print('Змея')
elif a == 2002 or a == 2014 or a == 2026:
  print('Лошадь')
elif a == 2003 or a == 2015 or a == 2027:
  print('Коза')
elif a == 2004 or a == 2016 or a == 2028:
  print('Обезьяна')
elif a == 2005 or a == 2017 or a == 2029:
  print('год петуха')
elif a == 2006 or a == 2018 or a == 2030:
  print('год Собаки')
elif a == 2007 or a == 2019 or a == 2031:
  print('год Свиньи')
elif a == 2008 or a == 2020 or a == 2032:
  print('год крысы')
elif a == 2009 or a == 2021 or a == 2033:
  print('год быка')
elif a == 2010 or a == 2022 or a == 2034:
  print('год тигра')
elif a == 2011 or a == 2023 or a == 2035:
  print('год кролика')
printTimeStamp("Давлат Черновол")
