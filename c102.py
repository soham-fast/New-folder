import os
import shutil

sourcePath="C:/Users/Admin/Desktop/C102_assets-main"
destPath="C:/Users/Admin/Desktop/img"

fileList=os.listdir(sourcePath)
#print(fileList)

for file in fileList:
    name,ext=os.path.splitext(file)
    #print(name)
    #print(ext)
    if ext == '':
        continue
    if ext in ['.gif','.png','.jpg','.jfif']:
        path1=sourcePath+"/"+file
        path2=destPath+'/'+file
        shutil.move(path1,path2)
        print(path1)
        print(path2)