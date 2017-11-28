# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 16:24:37 2017

@author: Administrator
"""
#根据xml文件，移动仅有ignore标签的图片
import os, os.path
import shutil

xmlpath = r'F:\AGraduateLab\Adata\ing\only_ignore\deletxml_file'
jpgpath = r'F:\AGraduateLab\Adata\ing\JPEGImages'

xmllist = os.listdir(xmlpath)

for xml in xmllist:
    jpg = xml.split('.')[0] +'.jpg'
    jpg_from = os.path.join(jpgpath, jpg)
    shutil.move(jpg_from, r'F:\AGraduateLab\Adata\ing\delete_img')