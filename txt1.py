# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:35:19 2020

@author: lfy15
"""
import numpy as np
import os
import re
import scipy.io as io
def result_analysis(path):
    f = open(path,'r')
    lines = f.readlines()
    c = []
    for line in lines:
        if "matchratio" in line:
            yy = line.strip().split(" ")
            for x in yy:
                c.append(re.findall(r'\d+',x))                
    all = []
    for tt in c:
        if(tt):
             all.append(tt)
    all = np.array(all)
    all = all.reshape(-1,24)
    print(all)
 #   io.savemat('D:\\txt1.mat', {'name': all})         
if __name__ == '__main__':
   #将文件夹路径作为参数传入
    result_analysis(r"C:\Users\lfy15\Desktop\1\FAR_1735_11_11_1_1.txt")   
     
                
                
            
            