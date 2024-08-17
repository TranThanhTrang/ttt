# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:28:59 2024

@author: Administrator
"""

a=float(input("nhap a la:"))
b=float(input("nhap b la:"))
c=float(input("nhap c la:"))
if a==0 or b==0 or c==0 :
    print("3 canh tren khong tao thanh 1 tam giac")
elif a+b>c and a+c>b and b+c>a :
    print(" 3 canh tren tao thanh 1 tam giac")
else:
    print(" 3 canh tren khong tao thanh 1 tam giac")
