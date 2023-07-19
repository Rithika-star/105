import os
import cv2

path = "images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
img=cv2.imread(images[0])
print(img.shape)
outputvideo=cv2.VideoWriter('video.mp4',cv2.VideoWriter_fourcc(*'DIVX'),5,(1280,720))
for i in range(count-1,0,-1):
    frame=cv2.imread(images[i])
    outputvideo.write(frame)
outputvideo.release()
print("Video successful")    
