#! /usr/bin/python3

import os
import pandas as pd

nameList = [nList for nList in os.listdir('.') if nList[-3:]=='csv']
# os.listdir()列出当前文件夹的文件和文件夹，不包括子文件夹
# os.walk()包括子文件夹

index = 0   # 配合第一个文件的特殊操作
col = 1     # 提取第几列
for fileName in nameList:
    tempFile = pd.read_csv(fileName, usecols=[col])
    if index == 0:
        outFile = tempFile
    else:
        outFile = pd.concat([outFile,tempFile],axis=1)
    index = index + 1

outFile.to_csv('multi.csv')


