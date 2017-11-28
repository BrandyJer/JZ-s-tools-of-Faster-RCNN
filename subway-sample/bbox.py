# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 16:43:45 2017

@author: Administrator
"""

#先创建一个存放打框图片的空文件夹===>本例中为：bbox1
#结合相应标记文件.xml给图片副本打框，查验标记的准确性

import xml.etree.ElementTree as ET
#import glob
import os, os.path
from PIL import Image, ImageDraw, ImageFont

SourcePath = "F:\\AGraduateLab\\AAA\\JPEGImages\\"#原pictnew图片路径
PathCopy_JPG = "F:\\AGraduateLab\\AAA\\bbox\\"#生成的打框图片存放路径
Path_xml = 'F:\\AGraduateLab\\AAA\\Annotations'#xml文件夹路径(只能有xml类型的文件)

MyType = ImageFont.truetype(r"C:\Windows\Fonts\SIMLI.TTF", 22)

for Xmlfile in os.listdir(Path_xml):
#items = glob.glob(Path_xml+'*.xml')

#for item in items:
    #解析.xml中的标记坐标
    tree = ET.parse(os.path.join(Path_xml, Xmlfile))  #使用解析器打开xml文件
    root = tree.getroot()
    filename = root.find('filename').text
    avatar = Image.open(SourcePath + filename)
    drawAvatar = ImageDraw.Draw(avatar)
    
    object_tree = root.findall('object')
    for object_list in object_tree:
        #for blocks in object_list:
        boxName = object_list.find('name')
        boxText = boxName.text
        bndbox = object_list.find('bndbox')
        box_xmin = int(bndbox.find('xmin').text)
        box_ymin = int(bndbox.find('ymin').text)
        box_xmax = int(bndbox.find('xmax').text)
        box_ymax = int(bndbox.find('ymax').text)
        #根据解析出的标记坐标批量给图片副本打框    
        drawAvatar.rectangle([box_xmin, box_ymin,\
                              box_xmax, box_ymax], outline = 'green') 
        drawAvatar.text((box_xmin, box_ymax), boxText,\
                        font = MyType, fill = 'red')
    #xSize, ySize = avatar.size
#    drawAvatar.line([0, 0.33 * ySize, xSize, 0.33 * ySize],\
#        fill = (255, 100, 0), width = 3)
#    drawAvatar.line([0, 0.67 * ySize, xSize, 0.67 * ySize],\
#        fill = (255, 0, 0), width = 3)
    #del drawAvatar
    
    avatar.save(PathCopy_JPG + filename)