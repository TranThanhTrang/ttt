# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 18:23:41 2024

@author: Administrator
"""

import random
ban=input("ban chon gi? (bua,keo,bao): ")
cpt= random.choice(["keo","bua","bao"])
print("ban chon:",  {ban})
print("may chon:",  {cpt})
if cpt==ban:
    print("hoa")
elif ban=="keo" and cpt=="bua" or ban=="bua" and cpt=="bao" or ban=="bao" and cpt=="keo":
        print("ban thua roi")
else:    
        print("ban thang roi")