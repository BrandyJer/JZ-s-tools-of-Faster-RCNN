# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 08:33:43 2017

@author: Administrator
"""

import os, os.path

path = "F:\\AGraduateLab\\Adata\\ing\\img_test"
#file_jpg = os.listdir(path)
f = open(r'F:\AGraduateLab\Adata\ing\test.txt', 'a')
for file in os.listdir(path):
    if '.jpg' in file:
        jpgname = file.split('.')[0]
        txtname = jpgname+'\n'
        f.write(txtname)
f.close()