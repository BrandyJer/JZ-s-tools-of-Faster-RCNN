# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:09:33 2017

@author: Administrator
"""
import os,os.path
import xml.etree.ElementTree as ET
file_path = r'F:\AGraduateLab\data\Annotations'
xmllist = os.listdir(file_path)
i = 0
for file in xmllist:
    filepath = os.path.join(file_path,file)
    ET.parse(filepath)
    i = i+1