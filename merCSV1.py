#! /usr/bin/python3

import os
import sys
import pandas as pd

filePath = str(sys.argv[1])
col = int(sys.argv[2])
desFile = str(sys.argv[3])
# for i in sys.argv:
#     print(i)

# filePath = fileP
nameList = [nList for nList in os.listdir(filePath) if nList[-3:]=='csv']
index = 0
# col = colNum
colNameList = []

for fileName in nameList:

    tempFile = pd.read_csv(fileName, usecols=[col])

    colSrcName = tuple(tempFile.columns) #get old col name
    colDesName = fileName[:-4]
    colNameList.append(colDesName)
    if index == 0:
        outFile = tempFile
    else:
        outFile = pd.concat([outFile,tempFile],axis=1)
    print(colNameList)
    outFile.columns=(colNameList)
    index = index + 1

outFile.to_csv(desFile)

