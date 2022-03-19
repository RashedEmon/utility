#This piece of python script helps a person to find the expected files from a bunch of files and copy them in a specific directory.
#It takes the path of a text file containing the expected file names. This script searches those files and copies them to the expected directory.

import os
import shutil
imageName=[]
image=[]
image=os.listdir("rfc/allpics")
print(image)
f=open("rfc/image.txt","r")
for item in f:
    arr=item.split("\n")
    imageName.append(arr[0])

print(imageName)

for item in imageName:
    item=f'{item}.jpg'
    if item in image:
        shutil.copy(f'rfc/allpics/{item}', "rfc/separate")
