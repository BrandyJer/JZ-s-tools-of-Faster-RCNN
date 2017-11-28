# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 09:41:21 2017

@author: Administrator
"""
#批量重命名
import os,os.path
import shutil
#注意：pict1中只能有图片类的文件
path_take = r'F:\AGraduateLab\pict1' #AApict文件夹下为原始图片（2万张图片）
path_rename = r'F:\AGraduateLab\pictnew1'   #AA文件夹下存重命名好的图片

jpglist = os.listdir(path_rename)
jpgtake = os.listdir(path_take)
jpgtake = sorted(jpgtake, 
                 key=lambda d : int(d.split('.')[0]))
for take in jpgtake[::10]:
    old = os.path.join(path_take, take)
    new = os.path.join(path_rename, '01_'+take)
    shutil.move(old, new)
#filenum = sorted(jpglist, 
#                 key=lambda d : int(d.split('.')[0])) #pict
#filenum = sorted(jpglist,
#                 key=lambda d : int(d.split('_')[-1].split('.')[0]))#3.22
#filenum = sorted(jpglist,
#                key=lambda d : int(d.split('MOV')[-1].split('.')[0]))
#for file in jpglist:
#    oldfile = os.path.join(path_rename, file)
##    str_x = str(x)
##    newname = str_x.rjust(6, '0')
#    newfile = os.path.join(path_rename, '03_'+file)#‘03’=>每处理一个文件夹加1
#    os.rename(oldfile, newfile)
    