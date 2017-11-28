# -*- coding: utf-8 -*-
"""
Created on Sun Jul 02 15:34:28 2017

@author: Administrator
"""
import os, os.path
import shutil
import random

#path = r'F:\AGraduateLab\Adata\ing\JPEGImages'
path = r'F:\AGraduateLab\Adata\ing\img_val'
listjpg = os.listdir(path)
catchlist = random.sample(listjpg, 206)

for catch in catchlist:
    jpg_from = os.path.join(path, catch)
    shutil.move(jpg_from, r'F:\AGraduateLab\Adata\ing\img_test')
#import os, os.path
#f = open(r'F:\AGraduateLab\AA\dog_trainval.txt', 'r')
#ftrain = open(r'F:\AGraduateLab\AA\dog_train.txt', 'a')
#fval = open(r'F:\AGraduateLab\AA\dog_val.txt', 'a')
#line = f.readline()
#x = 0
#while line:
#    if x <= 7:
#        ftrain.write(line)
#        x = x+1
#        line = f.readline()
#    if x >= 8:
#        fval.write(line)
#        x = x+1
#        line = f.readline()
#        if x == 10:
#            x = 0
#f.close()
#ftrain.close()
#fval.close()         
#    