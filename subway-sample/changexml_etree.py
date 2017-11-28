# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:10:10 2017

@author: Administrator
"""

import xml.etree.ElementTree as ET
import glob

path = 'F:\\AGraduateLab\pictnew1\\xml\\'

items = glob.glob(path+'*.xml')

trainval_txt = 'F:\\AGraduateLab\\pictnew1\\trainval_1.txt'#生成trainval.txt文件

for item in items:
    tree = ET.parse(item)   #使用解析器打开xml文件
    root = tree.getroot()
    #print root.tag
    
#    for child in root:
#        print child.tag
    folder_tree = root.find('folder')
    folder_tree.text = 'VOC2007'
    #print folder_tree.text
    
    image_tree = root.find('filename')
    with open(trainval_txt, 'a+') as f:
        f.write(image_tree.text)
        f.write('\n')
    image_tree.text = image_tree.text + '.jpg'
    
    path_tree = root.find('path')
    root.remove(path_tree)
    
    source_tree = root.find('source')
    
    database_tree = source_tree.find('database')
    database_tree.text = 'The VOC2007 Database'
    database_tree.tail = '\n' + '\t'*2
    
    annotation_tree = ET.SubElement(source_tree, 'annotation')
    annotation_tree.text = 'PASCAL VOC2007'
    annotation_tree.tail = '\n' + '\t'*2
    image_tree = ET.SubElement(source_tree, 'image')
    image_tree.text = 'flickr'
    image_tree.tail = '\n' + '\t'
    
    with open(item, 'w') as f:
        tree.write(f, encoding='utf-8', xml_declaration=False)
