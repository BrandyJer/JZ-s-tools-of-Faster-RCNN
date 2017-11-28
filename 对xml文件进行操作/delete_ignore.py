# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:10:10 2017

@author: Administrator
"""
###删除ignore类样本，移动只有ignore类样本的xml文件###

import os, os.path
import shutil
import xml.etree.ElementTree as ET
import glob

object_num = 0
headshoulder_num = 0

path = 'F:\\AGraduateLab\\Adata\\ing\\Annotations\\'

items = glob.glob(path+'*.xml')

for item in items:
    tree = ET.parse(item)   #使用解析器打开xml文件
    root = tree.getroot()

    object_tree = root.findall('object')
    for object_list in object_tree:
        name = object_list.find('name')
        if name.text == 'headshoulder':
            object_num = object_num+1
            headshoulder_num = headshoulder_num+1
        if name.text == 'ignore':
#            object_list.find('difficult').text = '1'
            root.remove(object_list)
            
    
    with open(item, 'w') as f:
        tree.write(f, encoding='utf-8', xml_declaration=False)
        
    #如果headshoulder=0,则移动该xml====>deletxml_file
    if object_num == 0:
        xmlpath = os.path.join(r"F:\AGraduateLab\Adata\ing\Annotations", item)
        shutil.move(xmlpath, r'F:\AGraduateLab\Adata\ing\deletxml_file')
    else:
        object_num = 0

print headshoulder_num
