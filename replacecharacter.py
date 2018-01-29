#-*- coding: UTF-8 -*- 


import os
import string

def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filepath, allDir))
        print (child) 
        print (allDir)

def readFile(filename):
    fopen = open(filename, 'r') 
    for eachLine in fopen:
        print ("read：",eachLine)
    fopen.close()

def writeFile(filename):
    pathDir = os.listdir(filename)
    output = open("D:/Ameba-Z2 platform/bitfile/vcd/output.txt",'w')
    print ("begin to write")
    newindex = 0
    pointer = 0
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filename, allDir))
        fopen = open(child, 'r')
        str1 = '#'
        str2 = '$'
        str3 = ' '
        for eachLine in fopen:
            if ((eachLine.find(str2) == 0)and( pointer > 1)):
                continue
            if ((eachLine.find(str3) == 0)and( pointer > 1)):
                continue
            data = eachLine.strip()
            if ((len(data) == 0)and( pointer > 1)):
                continue
            if eachLine.find(str1) == 0:
                newLine = '#%d' % newindex
                output.write('%s\n' % newLine)
                newindex = newindex+1
            else:
                output.write('%s' % eachLine)
        fopen.close()
        pointer = pointer + 1
if __name__ == '__main__':
    filePath = "D:/Ameba-Z2 platform/bitfile/vcd/s.1.vcd"
    filePathI = "D:/Ameba-Z2 platform/bitfile/vcd"
    filePathC = "D:/Ameba-Z2 platform/bitfile/vcd"
    eachFile(filePathC)
    #readFile(filePath)
    writeFile(filePathI)
