# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 07:19:59 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:49:33 2017

@author: Administrator
"""

import xml.dom.minidom as Dom
import re
from PIL import Image

f = open(r'F:\AGraduateLab\AA\pangxuece\pictnew1\label_new1.txt','rb')
#mydict = {}
lines = f.readlines()

for i in range(len(lines)):
    if 'SQUARE' in lines[i]:         
        splitLine = lines[i].split(':')
        #mydict[splitLine[0]] = splitLine[1]
        if (int(splitLine[1]) != 0):
            splitLine2 = lines[i-1].split(':')
            splitLine3 = splitLine2[1].split('.')
            img = Image.open(splitLine3[0]+".jpg")
            new=str(img.size)
            new1 = new.split(',') 
            wid = new1[0].split('(')
            hei = new1[1].split(')')
            
            if __name__ == "__main__":
                doc = Dom.Document()  
                root_node = doc.createElement("annotation")  
                
                doc.appendChild(root_node)  
  
 
                book_name_node = doc.createElement("folder")  
                book_name_value = doc.createTextNode("VOC2007")  
                book_name_node.appendChild(book_name_value)  
                root_node.appendChild(book_name_node)  
 
                book_author_node = doc.createElement("filename")  
                book_author_value = doc.createTextNode(splitLine2[1]+"")  
                book_author_node.appendChild(book_author_value)  
                root_node.appendChild(book_author_node)  
                
                book_node = doc.createElement("source")  
                book_data_node = doc.createElement("database")
                book_data_value = doc.createTextNode("The VOC2007 Database")
                book_data_node.appendChild(book_data_value)
                book_node.appendChild(book_data_node)
                
                book_anno_node = doc.createElement("annotation")
                book_anno_value = doc.createTextNode("PASCAL VOC2007")
                book_anno_node.appendChild(book_anno_value)
                book_node.appendChild(book_anno_node)
                
                book_img_node = doc.createElement("image")
                book_img_value = doc.createTextNode("flickr")
                book_img_node.appendChild(book_img_value)
                book_node.appendChild(book_img_node)
                
                root_node.appendChild(book_node)
                
                book_node1 = doc.createElement("size")  
                book_wid_node1 = doc.createElement("width")
                book_wid_value = doc.createTextNode(wid[1]+"")
                book_wid_node1.appendChild(book_wid_value)
                book_node1.appendChild(book_wid_node1)
                                
                book_hei_node1 = doc.createElement("height")
                book_hei_value = doc.createTextNode(hei[0]+"")
                book_hei_node1.appendChild(book_hei_value)
                book_node1.appendChild(book_hei_node1)
                                 
                book_dep_node1 = doc.createElement("depth")
                book_dep_value = doc.createTextNode("3")
                book_dep_node1.appendChild(book_dep_value)
                book_node1.appendChild(book_dep_node1)
                
                root_node.appendChild(book_node1)
                
                book_seg_node = doc.createElement("segmented")  
                book_seg_value = doc.createTextNode("0")  
                book_seg_node.appendChild(book_seg_value)  
                root_node.appendChild(book_seg_node) 
                 
                
                for n in range(0,int(splitLine[1])):                                                       
                    book_ob_node = doc.createElement("object") 
                    book_name1_node = doc.createElement("name")
                    book_name1_value = doc.createTextNode("person")
                    book_name1_node.appendChild(book_name1_value)
                    book_ob_node.appendChild(book_name1_node)
                    
                    book_pose_node = doc.createElement("pose")
                    book_pose_value = doc.createTextNode("Unspecified")
                    book_pose_node.appendChild(book_pose_value)
                    book_ob_node.appendChild(book_pose_node)
                    
                    book_trun_node = doc.createElement("truncated")
                    book_trun_value = doc.createTextNode("0")
                    book_trun_node.appendChild(book_trun_value)
                    book_ob_node.appendChild(book_trun_node)
                    
                    book_diff_node = doc.createElement("difficult")
                    book_diff_value = doc.createTextNode("0")
                    book_diff_node.appendChild(book_diff_value)
                    book_ob_node.appendChild(book_diff_node)
                    
                    
                    posx = lines[i+3+n*6].split(':')
                    posy = lines[i+4+n*6].split(':')
                    size = lines[i+5+n*6].split(' ')
                    trans_posx=int(posx[1])
                    trans_size=int(size[1])
                    trans_posy=int(posy[1])
                    posx1 = int(posx[1])+1
                    posy1 = int(posy[1])+1
                    posx11 = str(posx1)
                    posy11 = str(posy1)
                    trans_x=trans_posx+trans_size
                    trans_y=trans_posy+trans_size
                    fin_x=str(trans_x)
                    fin_y=str(trans_y)
                   
                    book_bnd_node = doc.createElement("bndbox") 
                    book_x_node = doc.createElement("xmin")
                    book_x_value = doc.createTextNode(posx11+"")
                    book_x_node.appendChild(book_x_value)
                    book_bnd_node.appendChild(book_x_node)
                    
                    book_y_node = doc.createElement("ymin")
                    book_y_value = doc.createTextNode(posy11+"")
                    book_y_node.appendChild(book_y_value)
                    book_bnd_node.appendChild(book_y_node)                
                    
                    book_xm_node = doc.createElement("xmax")
                    book_xm_value = doc.createTextNode(fin_x+"")
                    book_xm_node.appendChild(book_xm_value)
                    book_bnd_node.appendChild(book_xm_node)
                    
                    book_ym_node = doc.createElement("ymax")
                    book_ym_value = doc.createTextNode(fin_y+"")
                    book_ym_node.appendChild(book_ym_value)
                    book_bnd_node.appendChild(book_ym_node)
                    
                    book_ob_node.appendChild(book_bnd_node)
                    
                    
                    
                    root_node.appendChild(book_ob_node)
                    
                
                
                n=open(splitLine3[0]+".xml","w")
                n.write(doc.toprettyxml(indent = "\t", newl = "\n", encoding = "utf-8")) 
                n.close()
            