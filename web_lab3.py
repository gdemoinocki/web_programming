# coding=windows-1251
import math

def error0(n):
    try:
        int(n)
    except ValueError:
        print("������� �����")
        return 0
    return 1

def error1(m):
    if error0(m) == 0:
        return 0 
    elif int(m) >= 0:
        return 1
    else:
        print("������� ������������� �����")
        return 0    


while(True):
    kat1 = input('������� ������ ������� ������: ')
    kat2 = input('������� ������ ������� ������: ')
    if error1(kat1)==1 and error1(kat2):
        kat1 = int(kat1)
        kat2= int(kat2)
        S = round((kat1 + kat2) /2, 2)
        hip = round(math.sqrt((kat1**2) + (kat2**2)),2)
        P = round((kat1 + kat2 + hip), 2)

        print('������ ����� =',kat1)
        print('������ ����� =',kat2)
        print('���������� = sqrt(', kat1, '^2 + ', kat2, '^2) = ', hip)
        print('������� �������������� ������������ = (', kat1, '+', kat2,')/2 = ', S)
        print('�������� �������������� ������������ =', kat1, '+', kat2, '+', hip, ' = ', P)

    
  