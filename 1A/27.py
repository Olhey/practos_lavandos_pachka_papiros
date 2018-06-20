import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
u = list(input("Введите два значения: Говорит ли попугай (Да/Нет) и время (HH:MM) через пробел: ").split())
b = u[1].split(r':')
a = ['22','23', '00', '01', '02', '03', '04', '05', '06', '07', '08']
if u[0] == "Да" and b[0] in a:
    print("Стоит накрыть клетку попугая простыней, чтобы он успокоился")
else:
    print("Накрывать клетку нет потребности")
printTimeStamp("Сергій Михайлов")