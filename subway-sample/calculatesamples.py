# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 16:43:45 2017

@author: Administrator
"""

#根据解析xml计算各类样本数量

import xml.etree.ElementTree as ET
#import glob
import os, os.path
#backhead_num = 0
#blockedhead_num = 0
#halfhead_num = 0
#sidehead_num = 0
headshoulder_num = 0
ignore_num = 0
file_num = 0

#xml文件夹路径(只能有xml类型的文件)
Path_xml = 'F:\\AGraduateLab\\Adata\\ing\\Annotations\\'

for Xmlfile in os.listdir(Path_xml):
#items = glob.glob(Path_xml+'*.xml')

#for item in items:
    #解析.xml中的标记坐标
    tree = ET.parse(os.path.join(Path_xml, Xmlfile))  #使用解析器打开xml文件
    root = tree.getroot()
    #filename = root.find('filename').text
    
    object_tree = root.findall('object')
    for object_list in object_tree:
        #for blocks in object_list:
        boxName = object_list.find('name')
        boxText = boxName.text
        if boxText=='headshoulder':
            headshoulder_num = headshoulder_num+1
        if boxText=='ignore':
            ignore_num = ignore_num+1
            
    file_num = file_num+1
    
print file_num
print headshoulder_num
print ignore_num
#        if boxText=='backhead':
#            backhead_num = backhead_num+1
#        if boxText=='blockedhead':
#            blockedhead_num = blockedhead_num+1
#        if boxText=='halfhead':
#            halfhead_num = halfhead_num+1
#        if boxText=='sidehead':
#            sidehead_num = sidehead_num+1
        
    #xSize, ySize = avatar.size
#    drawAvatar.line([0, 0.33 * ySize, xSize, 0.33 * ySize],\
#        fill = (255, 100, 0), width = 3)
#    drawAvatar.line([0, 0.67 * ySize, xSize, 0.67 * ySize],\
#        fill = (255, 0, 0), width = 3)
    #del drawAvatar