#! /usr/bin/python3

import os
import sys
import pandas as pd

def mergeCSV(fileP, colNum, desFile):
    fileP = str(sys.argv[1])
    colNum = int(sys.argv[2])
    desFile = str(sys.argv[3])
    for i in sys.argv:
        print(i)
    filePath = fileP
    nameList = [nList for nList in os.listdir(filePath) if nList[-3:]=='csv']
    index = 0
    col = colNum

    for fileName in nameList:

        tempFile = pd.read_csv(fileName, usecols=[col])

        colSrcName = list(tempFile) #get old col name
        colDesName = fileName[:-4]

        if index == 0:
            outFile = tempFile
        else:
            outFile = pd.concat([outFile,tempFile],axis=1)

        outFile.rename(columns={colSrcName:colDesName})
        index = index + 1

    outFile.to_csv(desFile)


