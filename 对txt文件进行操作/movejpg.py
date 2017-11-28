# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 20:38:37 2017

@author: Administrator
"""

import os, os.path
import shutil
#os.rmdir(r'F:\AGraduateLab\AA\trainsubway')
jpg = 'img_00000'+'.jpg'
#os.mkdir(r'F:\AGraduateLab\AA\trainsubway')
jpgpath = os.path.join("F:\\AGraduateLab\\AA\\3.22\\20130314\\00088", jpg)#将分离的各部分组合成一个路径名
shutil.move(jpgpath, "F:\\AGraduateLab\\AA\\trainsubway")