# -*- coding: utf-8 -*-
"""
Created on Wed Jul 05 14:10:53 2017

@author: Administrator
"""

import xml.dom.minidom as xdm
import glob

path = 'F:\\AGraduateLab\\AA\\'

items = glob.glob(path+'*.xml')

train_txt = 'train.txt'

for item in items:
    dom = xdm.parse(item)   #使用解析器打开xml文件
    root = dom.documentElement

    # change folder name
    folder_dom = root.getElementsByTagName('folder')
#    print folder_dom[0].firstChild.data
    folder_dom[0].firstChild.data = 'VOC2007'

    # change image name
    image_dom = root.getElementsByTagName('filename')
    print image_dom[0].firstChild.data

    with open(train_txt, 'a+') as f:
        f.write(image_dom[0].firstChild.data)
        f.write('\n')

    image_dom[0].firstChild.data = image_dom[0].firstChild.data + '.jpg'
    with open(item, 'w') as f:
        dom.writexml(f, encoding='utf-8')
