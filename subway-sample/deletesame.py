# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 21:42:46 2017

@author: Administrator
"""
#删除txt文件中相同的行，以防同一张图片有相同的标签
fw = open(r'F:\AGraduateLab\AA\pangxuece\pict2\new.txt', 'a')
with open(r'F:\AGraduateLab\AA\pangxuece\pict2\label.txt', 'r') as f:
    linepre = f.readline()
    line = linepre
    fw.write(line)
    while line:
        if line == linepre:
            line = f.readline()
        else:
            fw.write(line)
            linepre = line
            line = f.readline()
fw.close()