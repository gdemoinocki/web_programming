# coding=windows-1251
import math

#проверка на тип int
def error0(n):
    try:
        int(n)
    except ValueError:
        print("Введите число")
        return 0
    return 1
    
#проверка на положительное число
def error1(m):
    if error0(m) == 0:
        
        return 0 
    elif int(m) >= 0:
        return 1
    else:
        print("Введите положительное число")
        return 0    

while(True):
    kat1 = input('введите длинну первого катета: ')
    if error1(kat1)==0:
        continue
    
    kat2 = input('Введите длинну второго катета: ')
    if error1(kat2)==0:
        continue
    
    else:
        kat1 = int(kat1)
        kat2= int(kat2)
        S = round((kat1 + kat2) /2, 2)
        hip = round(math.sqrt((kat1**2) + (kat2**2)),2)
        P = round((kat1 + kat2 + hip), 2)

        print('Первый катет =',kat1)
        print('Второй катет =',kat2)
        print('Гипотенуза = sqrt(', kat1, '^2 + ', kat2, '^2) = ', hip)
        print('Площадь прямоугольного треугольника = (', kat1, '+', kat2,')/2 = ', S)
        print('Периметр прямоугольного треугольника =', kat1, '+', kat2, '+', hip, ' = ', P)
