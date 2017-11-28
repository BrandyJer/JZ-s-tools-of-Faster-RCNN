# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:10:10 2017

@author: Administrator
"""
###修改使用中科院标定工具产生的xml文件###

import xml.etree.ElementTree as ET
import glob

path = 'F:\\AGraduateLab\\data\\Adata\\annotations\\'

items = glob.glob(path+'*.xml')
#生成trainval.txt文件
trainval_txt = 'F:\\AGraduateLab\\data\\Adata\\ImageSets\\trainval.txt'

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
    #image_tree.text = image_tree.text + '.jpg'
    
    #path_tree = root.find('path')
    #root.remove(path_tree)
    owner_tree = root.find('owner')
    root.remove(owner_tree)
    
    source_tree = root.find('source')
    
    database_tree = source_tree.find('database')
    database_tree.text = 'The VOC2007 Database'
    
    annotation_tree = source_tree.find('annotation')
    annotation_tree.text = 'PASCAL VOC2007'
    
    image_tree = source_tree.find('image')
    image_tree.text = 'flickr'
    
#    flickrid_tree = source_tree.find('flickrid')
#    source_tree.remove(flickrid_tree)

#
    object_tree = root.findall('object')
    for object_list in object_tree:
        name = object_list.find('name')
        if name.text == 'ignore':
            object_list.find('difficult').text = '1'
            
        bndbox = object_list.find('bndbox')
        
        xmin = bndbox.find('xmin')
        box_xmin = int(xmin.text)
        box_xmin = str(box_xmin+1)
        xmin.text = box_xmin
        
        ymin = bndbox.find('ymin')
        box_ymin = int(ymin.text)
        box_ymin = str(box_ymin+1)
        ymin.text = box_ymin
        
#    database_tree = source_tree.find('database')
#    database_tree.text = 'The VOC2007 Database'
#    database_tree.tail = '\n' + '\t'*2
    
#    annotation_tree = ET.SubElement(source_tree, 'annotation')
#    annotation_tree.text = 'PASCAL VOC2007'
#    annotation_tree.tail = '\n' + '\t'*2
#    image_tree = ET.SubElement(source_tree, 'image')
#    image_tree.text = 'flickr'
#    image_tree.tail = '\n' + '\t'
    
    with open(item, 'w') as f:
        tree.write(f, encoding='utf-8', xml_declaration=False)
