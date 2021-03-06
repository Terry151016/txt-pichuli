# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:45:25 2020

@author: lfy15
"""
import numpy as np
import os
import re
import scipy.io as io
dir_path=r"C:\Users\lfy15\Desktop\FAR_1735_11_11_1_1.txt"
p1 = re.compile(r'(?<=matchratio =)\s*\d')
out1 = []
p2 = re.compile(r'(?<=matchsize =)\s*\d')
out2 = []
p3 = re.compile(r'(?<=matchnum =)\s*\d')
out3 = []
p4 = re.compile(r'(?<=sim_score = )\d*')
out4 = []
p5 = re.compile(r'(?<=sim_score1 = )\d*')
out5 = []
p6 = re.compile(r'(?<=diff_score1 = )\d*')
p61 = re.compile(r'(?<=diff_score1 = -)\d*')
out6 = []
p7 = re.compile(r'(?<=maxnum=)\d*')
out7 = []
p8 = re.compile(r'(?<=M_ratio=)\d*')
out8 = []
p9 = re.compile(r'(?<=num_reg=)\d*')
out9 = []
p10 = re.compile(r'(?<=num_rec=)\d*')
out10 = []
p11 = re.compile(r'(?<=tttt=)\d*')
p111 = re.compile(r'(?<=tttt=-)\d*')
out11 = []
p12 = re.compile(r'(?<=i=)\d*')
out12 = []
p13 = re.compile(r'(?<=ount_i=)\d*')
out13 = []
p14 = re.compile(r'(?<=Area=)\d*')
out14 = []
p15 = re.compile(r'(?<=in_7=)\d*')
out15 = []
p16 = re.compile(r'(?<=in_8=)\d*')
out16 = []
p17 = re.compile(r'(?<=sim_3=)\d*')
out17 = []
p18 = re.compile(r'(?<=t90_5=)\d*')
out18 = []

with open(dir_path, encoding='utf-8') as file:
    for line in file.readlines():
        s1 = p1.findall(line)
        s2=p2.findall(line)
        s3=p3.findall(line)
        s4=p4.findall(line)
        s5=p5.findall(line)
        s6=p6.findall(line)
        s61=p61.findall(line)
        s7=p7.findall(line)
        s8=p8.findall(line)
        s9=p9.findall(line)
        s10=p10.findall(line)       
        s11=p11.findall(line)
        s111=p111.findall(line)
        s12=p12.findall(line)
        s13=p13.findall(line)
        s14=p14.findall(line)
        s15=p15.findall(line)
        s16=p16.findall(line)
        s17=p17.findall(line)
        s18=p18.findall(line)
        
        if s1:
            out1.append(eval(s1[0]))
        if s2:
            out2.append(eval(s2[0]))
        if s3:
            out3.append(eval(s3[0]))    
        if s4:
            out4.append(eval(s4[0]))
        if s5:
            out5.append(eval(s5[0]))
        if s6:
            if s61:
                out6.append('-'+''.join(s61))
            else:
                out6.append(eval(s6[0]))
        if s7:
            out7.append(eval(s7[0]))  
        if s8:
            out8.append(eval(s8[0]))  
        if s9:
            out9.append(eval(s9[0]))  
        if s10:
            out10.append(eval(s10[0]))  
        if s11:
            if s111:
                out11.append('-'+''.join(s111))
            else:
                out11.append(eval(s11[0]))
        if s12:
            out12.append(eval(s12[0]))
        if s13:
            out13.append(eval(s13[0]))
        if s14:
            out14.append(eval(s14[0]))
        if s15:
            out15.append(eval(s15[0]))
        if s16:
            out16.append(eval(s16[0]))
        if s17:
            out17.append(eval(s17[0]))
        if s18:
            out18.append(eval(s18[0]))
out01 = np.transpose(out1)
out22 = np.transpose(out2)
out33 = np.transpose(out3)
out44 = np.transpose(out4)
out55 = np.transpose(out5)
out66 = np.transpose(out6)
out77 = np.transpose(out7)
out88 = np.transpose(out8)
out99 = np.transpose(out9)
out110 = np.transpose(out10)
out111 = np.transpose(out11)
out112 = np.transpose(out12)
out113 = np.transpose(out13)
out114 = np.transpose(out14)
out115 = np.transpose(out15)
out116 = np.transpose(out16)
out117 = np.transpose(out17)
out118 = np.transpose(out18)
print(out01)
print(out22)
print(out33)
print(out44)
print(out55)
print(out66)
print(out77)
print(out88)
print(out99)
print(out110)
print(out111)
print(out112)
print(out113)
print(out114)
print(out115)
print(out116)
print(out117)
print(out118)

d = np.vstack((out01,out22,out33,out44,out55,out66,out77,out88,out99,out110,out111,out112,out113,out114,out115,out116,out117,out118))
print(d)
mat = d
io.savemat('D:\\txt.mat', {'name': mat})

