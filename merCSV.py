# -*- coding: UTF-8 -*-
#! /usr/bin/python2

# v1.3.20191213
# 引入 if __name__ == "__main__", 即将脚本内容都定义为函数, 提供函数执行入口

import os
import sys
import pandas as pd
import datetime
import numpy as np

def days(filePath, col, desFile):
    pass

def merCSV(filePath, col, desFile):

    desFile = filePath+desFile

    nameList = [nList for nList in os.listdir(filePath) if nList[-3:]=='csv']
    
    # col = colNum
    # colNameList = []
    i = 0
    date_0 = datetime.datetime(2013, 1, 1)  # 将要输出的起始时间
    for fileName in nameList:
        # 计算导入文件所需NaN行数
        timeCol = pd.read_csv(filePath+fileName, usecols=[0])   # read time column
        date_marker = timeCol['time'][0]    # 读取时间列第一个数据
        # 将读取的str转化为时间
        date_1 = datetime.datetime(int(date_marker[0:4]), int(date_marker[5:7]), int(date_marker[8:10]))
        dayNum = (date_1 - date_0).days # 计算相差的天数，即为要插入的NaN行数

        # 设置城市名为列名
        colDesName = fileName[:-4]
        # 读取数据列，并将缺失时间补全为NaN
        dataFile = pd.read_csv(filePath+fileName, usecols=[col])
        dataFile.columns = [colDesName] # 统一列名为城市名
        nanFile = pd.DataFrame(np.full([dayNum,1], np.nan))
        nanFile.columns = [colDesName]  # 统一列名
        dataFile = pd.concat([nanFile, dataFile])
        # 修改数据列的行索引为数字
        dataFile.index = list(range(len(dataFile))) 
        
        # 将提取的数据合并
        # colNameList.append(colDesName)
        if i == 0:
            outFile = dataFile
        else:
            outFile = pd.concat([dataFile, outFile], axis=1)
        i += 1
        # print(colNameList)
        # outFile.columns=(colNameList)
    
    # 利用最后一组数据创建完整时间列
    endDate = date_marker[5:7] + '/' + str(int(date_marker[8:10])-1) + '/' + date_marker[0:4]
    subTime = pd.DataFrame(pd.date_range('01/01/2013', endDate))
    subTime.columns = ['Time']  # 修改列名
    timeCol.columns = ['Time']
    timeFile = pd.concat([subTime, timeCol])
    timeFile.index = list(range(len(timeFile)))

    # 添加时间序列至第一列
    outFile = pd.concat([timeFile, outFile], axis=1)   
    # 另存为新的csv文件 
    outFile.to_csv(desFile)

if __name__ == "__main__":
    merCSV(sys.argv[1], int(sys.argv[2]), sys.argv[3])