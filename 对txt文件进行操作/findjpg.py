# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 10:45:00 2017

@author: Administrator
"""

# 用来查找某个目录及其子目录的文件中包含某个字符串的文件名

import os, os.path
import sys

def search(path, str):
    for x in os.listdir(path):# 输出所有文件和文件夹
       fp = os.path.join(path, x)#将分离的各部分组合成一个路径名
       if os.path.isfile(fp):
          with open(fp, 'r') as fc:
             for line in fc.readlines():
               if str in line:
                 print fp
                 break
       #elif os.path.isdir(fp):#判断给出的路径是否是一个目录
        #  search(fp, str)

if len(sys.argv) == 1:
   print 'useage: search str'
elif len(sys.argv) == 2:
   str = sys.argv[1]
   search('.', str)
else:
   print 'too many parameters'