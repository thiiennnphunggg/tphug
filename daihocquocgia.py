# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:11:56 2024

@author: La Thiên Phụng 
"""

s="Đại học quốc gia, Khu phố 6, P.Linh Trung, Q.Thủ Đức, Tp.HCM"
s1=s.split(", ")
for i in s1:
    print(i)
s2=s.replace('P.','').replace('Q.','').replace('Tp. ','').split(", ")
for u in s2:
    print(u)