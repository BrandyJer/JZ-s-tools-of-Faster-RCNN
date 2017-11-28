# -*- coding: utf-8 -*-
"""
Created on Mon Jul 03 14:27:36 2017

@author: Administrator
"""

f = open(r'F:\AGraduateLab\AA\3.22\txt\00003.txt', 'r')
line = f.readline()
hang = 1
hanghao = 0
x = 0
while line:
    findnum = line.find(':')
    startnum = findnum-2
    re = line[startnum:findnum]
    if re == 'SX':
        num = line.split(':')[-1]
        num = int(num)
        if num == 0:
            x = x+1
            hanghao = hang
    line = f.readline()
    hang = hang+1
f.close()