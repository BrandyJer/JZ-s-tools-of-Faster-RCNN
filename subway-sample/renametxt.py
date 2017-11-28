# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 11:10:07 2017

@author: Administrator
"""

#在txt里修改rename的图片名
f_old = open(r'F:\AGraduateLab\AA\pangxuece\pictnew2\label_new2.txt', 'r')
f_new = open(r'F:\AGraduateLab\AA\pangxuece\pictnew2\pict02.txt', 'a')
line = f_old.readline()
while line:
    f_new.write('02_'+line)
    line = f_old.readline()
f_old.close()
f_new.close()