import os
import shutil

sourcePath="C:/Users/Admin/Desktop/p102"
destPath="C:/Users/Admin/Desktop/d102/docs"

fileList=os.listdir(sourcePath)
print(fileList)

for file in fileList:
    name,ext=os.path.splitext(file)
    if ext=='':
        continue
    if ext in ['.txt','.docx']:
        path1=sourcePath+'/'+file
        path2=destPath+'/'+file
        shutil.move(path1,path2)
        print(path1)
        print(path2)