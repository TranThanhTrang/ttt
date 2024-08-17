# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:36:10 2024

@author: Administrator
"""

a=float(input("nhap a la:"))
b=float(input("nhap b la:"))
c=float(input("nhap c la:"))
if a==0 or b==0 or c==0 :
    print("3 canh tren khong tao thanh 1 tam giac")
if a+b>c and a+c>b and b+c>a :
    if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2== a**2 :
        print("tam giac tren la tam giac vuong")
    elif (a==b and a!=c) or (a==c and a!=b) or (b==c and a!=b):
        print("tam giac tren la tam giac can")
    elif a==b and a==c:
        print("tam giac tren la tam giac deu")
    else:
        print(" tam giac tren la tam giac thuong")
else:
    print(" 3 canh tren khong tao thanh 1 tam giac")