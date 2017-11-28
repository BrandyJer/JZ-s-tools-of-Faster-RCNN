# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

f = open(r'F:\AGraduateLab\AA\txt\test.txt', 'r')
line = f.readline()             # 调用文件的 readline()方法
jpg = line
while line:
    if line == 'quit\n':
        print jpg[6:]                # 后面跟 ',' 将忽略换行符
    else:
        jpg = line
    line = f.readline()
f.close()