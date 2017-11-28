# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 17:46:11 2017

@author: Administrator
"""

import os,os.path

x = 5140
pathroot = 'I:\\flower\\JZworking\\subway\\pict\\pictxml'
#filenum = os.listdir(pathroot)
jpglist = os.listdir(pathroot)
filenum = sorted(jpglist, 
                 key=lambda d : int(d.split('.')[0])) #pict
#filenum = sorted(jpglist,
#                 key=lambda d : int(d.split('_')[-1].split('.')[0]))#3.22
#filenum = sorted(jpglist,
#                key=lambda d : int(d.split('MOV')[-1].split('.')[0]))
for file in filenum:
    oldfile = os.path.join(pathroot,file)
    str_x = str(x)
    newname = str_x.rjust(6, '0')
    newfile = os.path.join(pathroot, newname+'.xml')
    os.rename(oldfile, newfile)
    x = x+1
