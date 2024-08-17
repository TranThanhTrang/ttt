# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:17:02 2024

@author: Administrator
"""

so=float(input("so km di duoc la: "))
tien=float
if so==1:
    tien=20000
elif so==2 :
    tien=2*13000
elif so==3:
    tien=3*13000
elif so>=4 and so<8 :
    tien=3*13000+(so-3)*12000
else:
    tien=3*13000+(8-3)*12000+ (so-8)*10000
if tien>100000:
    tien=tien*0.92
print("so tien phai tra la:",tien)