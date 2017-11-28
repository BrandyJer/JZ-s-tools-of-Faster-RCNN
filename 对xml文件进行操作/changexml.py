# -*- coding: utf-8 -*-
"""
Created on Wed Jul 05 14:10:53 2017

@author: Administrator
"""

import xml.dom.minidom as xdm
import glob

path = 'F:\\AGraduateLab\\AA\\'

items = glob.glob(path+'*.xml')

trainval_txt = 'F:\\AGraduateLab\\AA\\trainval_3.txt'#生成trainval.txt文件

for item in items:
    dom = xdm.parse(item)   #使用解析器打开xml文件
    root = dom.documentElement
#    root_text = dom.createElement('\n')
#    root.parentNode.insertBefore(root_text, root)
    # change folder name
    folder_dom = root.getElementsByTagName('folder')
#    print folder_dom[0].firstChild.data
    folder_dom[0].firstChild.data = 'VOC2007'

    # change image name
    image_dom = root.getElementsByTagName('filename')
#    print image_dom[0].firstChild.data
    with open(trainval_txt, 'a+') as f:
        f.write(image_dom[0].firstChild.data)
        f.write('\n')
    image_dom[0].firstChild.data = image_dom[0].firstChild.data + '.jpg'
    
    path_dom = root.getElementsByTagName('path')
    root.removeChild(path_dom[0])
    
    source_dom = root.getElementsByTagName('source')
    
    database_dom = root.getElementsByTagName('database')
    database_dom[0].firstChild.data = 'The VOC2007 Database'
    
    annotation_dom = dom.createElement('annotation')
    annotation_value = dom.createTextNode('PASCAL VOC2007')
    annotation_dom.appendChild(annotation_value)
    source_dom[0].appendChild(annotation_dom)
    
    image_dom = dom.createElement('image')
    image_value = dom.createTextNode('flickr')
    image_dom.appendChild(image_value)
    source_dom[0].appendChild(image_dom)
    
    with open(item, 'w') as f:
        dom.writexml(f, encoding='utf-8')
