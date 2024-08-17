# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 12:47:13 2024

@author: Administrator
"""

so= float(input(" nhap diem trung binh GPA: "))
if  so < 3.5 and so>0:
    print("Hoc luc Kem")
elif so >=3.5 and so < 5:
    print(" hoc luc Yeu")
elif so >=5 and so<7:
    print("hoc luc trung binh")
elif so >=7 and so<8:
    print(" hoc luc kha")
elif so>=8 and so <9:
    print(" hoc luc gioi")
elif so >=9 and so<=10:
    print(" hoc luc xuat sac")
else:
        print(" khong xac dinh")
    