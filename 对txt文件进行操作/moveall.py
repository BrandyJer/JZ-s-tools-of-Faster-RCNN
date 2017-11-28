# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 15:36:30 2017

@author: Administrator
"""
import os, os.path
import shutil
f = open(r'F:\AGraduateLab\AA\jietutxt\10.txt', 'r')
line = f.readline()             # 调用文件的 readline()方法
jpg = line
#while line:
#    if line == 'SQUARE:0\n':
#        #jpg = jpg[9:18]+'.jpg'
#        startnum = jpg.find(':')
#        startnum = startnum+1
#       endnum = startnum+13 #+9=>with3.22
#       jpg = jpg[startnum:endnum]+'.jpg'
#       jpgpath = os.path.join("F:\\AGraduateLab\\AA\\jietu\\paishe15", jpg)#将分离的各部分组合成一个路径名
#       shutil.move(jpgpath, "F:\\AGraduateLab\\AA\\unuseing\\paishe15")
#   else:
#       jpg = line     #存上一行内容
#   line = f.readline()
while line:
    findnum = line.find(':')
    startnum = findnum-2
    re = line[startnum:findnum]
    if re == 'RE':
        num = findnum+1
        num = int(line[num])
        if num > 0:
            snum = jpg.find(':')
            snum = snum+1
            enum = snum+16  #snum已经+1
            jpg = jpg[snum:enum]+'.jpg'
            jpgpath = os.path.join("F:\\AGraduateLab\\AA\\jietu\\10", jpg)#将分离的各部分组合成一个路径名
            shutil.move(jpgpath, "F:\\AGraduateLab\\AA\\jietuuseing\\10")
    else:
       jpg = line     #存上一行内容
    line = f.readline()
f.close()
